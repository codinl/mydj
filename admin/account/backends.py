from admin.account.models import Admin

class ModelBackend(object):
    """
    Authenticates against django.contrib.auth.models.Admin.
    """
    supports_inactive_admin = True

    # TODO: Model, login attribute name and password attribute name should be
    # configurable.
    def authenticate(self, name=None, password=None):
        try:
            admin = Admin.objects.get(name=name)
            if admin.check_password(password):
                return admin
        except Admin.DoesNotExist:
            return None


    def get_admin(self, admin_id):
        try:
            return Admin.objects.get(pk=admin_id)
        except Admin.DoesNotExist:
            return None

