from django.utils.functional import SimpleLazyObject
import account


def get_user(request):
    if not hasattr(request, '_cached_user'):
        request._cached_user = account.get_user(request)
    return request._cached_user

class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        request.user = SimpleLazyObject(lambda: get_user(request))
