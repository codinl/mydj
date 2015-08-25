from admin import account
from django.utils.functional import SimpleLazyObject

def get_admin(request):
    if not hasattr(request, '_cached_admin'):
        request._cached_admin = account.get_admin(request)
    return request._cached_admin

class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        request.admin = SimpleLazyObject(lambda: get_admin(request))
