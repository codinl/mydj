from django.dispatch import Signal

admin_logged_in = Signal(providing_args=['request', 'admin'])
admin_logged_out = Signal(providing_args=['request', 'admin'])