from admin.account.models import AnonymousAdmin
from admin.account.signals import admin_logged_in, admin_logged_out
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from warnings import warn

SESSION_KEY = '_account_admin_id'
BACKEND_SESSION_KEY = '_account_admin_backend'
REDIRECT_FIELD_NAME = 'next'

def load_backend(path):
    i = path.rfind('.')
    module, attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured('Error importing authentication backend %s: "%s"' % (path, e))
    except ValueError, e:
        raise ImproperlyConfigured('Error importing authentication backends. Is AUTHENTICATION_BACKENDS a correctly defined list or tuple?')
    try:
        cls = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" authentication backend' % (module, attr))

    if not hasattr(cls, 'supports_inactive_admin'):
        warn("Authentication backends without a `supports_inactive_admin` attribute are deprecated. Please define it in %s." % cls,
             DeprecationWarning)
        cls.supports_inactive_admin = False
    return cls()

def get_backends():
    import account_settings as settings
    backends = []
    for backend_path in settings.AUTHENTICATION_BACKENDS:
        backends.append(load_backend(backend_path))
    if not backends:
        raise ImproperlyConfigured('No authentication backends have been defined. Does AUTHENTICATION_BACKENDS contain anything?')
    return backends

def authenticate(**credentials):
    """
    If the given credentials are valid, return a Admin object.
    """
    for backend in get_backends():
        try:
            admin = backend.authenticate(**credentials)
        except TypeError,e:
            # This backend doesn't accept these credentials as arguments. Try the next one.
            continue
        if admin is None:
            continue
        # Annotate the admin object with the path of the backend.
        admin.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
        return admin

def login(request, admin):
    """
    Persist a admin id and a backend in the request. This way a admin doesn't
    have to reauthenticate on every request. Note that data set during
    the anonymous session is retained when the admin logs in.
    """
    if admin is None:
        admin = request.admin
    # TODO: It would be nice to support different login methods, like signed cookies.
    if SESSION_KEY in request.session:
        if request.session[SESSION_KEY] != admin.id:
            # To avoid reusing another admin's session, create a new, empty
            # session if the existing session corresponds to a different
            # authenticated admin.
            request.session.flush()
    else:
        request.session.cycle_key()
    request.session[SESSION_KEY] = admin.id
    request.session[BACKEND_SESSION_KEY] = admin.backend
    if hasattr(request, 'admin'):
        request.admin = admin
    admin_logged_in.send(sender=admin.__class__, request=request, admin=admin)

def logout(request):
    """
    Removes the authenticated admin's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the admin is logged out so the receivers have a
    # chance to find out *who* logged out.
    admin = getattr(request, 'admin', None)
    if hasattr(admin, 'is_authenticated') and not admin.is_authenticated():
        admin = None
    admin_logged_out.send(sender=admin.__class__, request=request, admin=admin)

    request.session.flush()
    if hasattr(request, 'admin'):
        request.admin = AnonymousAdmin()

def get_admin(request):
    try:
        admin_id = request.session[SESSION_KEY]
        backend_path = request.session[BACKEND_SESSION_KEY]
        backend = load_backend(backend_path)
        admin = backend.get_admin(admin_id) or AnonymousAdmin()
    except KeyError:
        admin = AnonymousAdmin()
    return admin
