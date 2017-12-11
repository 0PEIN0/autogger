from user.models import *

from django.conf import settings

admin_user_email = settings.DJANGO_ADMIN_SUPER_USER_EMAIL
admin_user_password = settings.DJANGO_ADMIN_SUPER_USER_PASSWORD

if not User.objects.filter(email=admin_user_email).exists():
    User.objects.create_superuser(
        email=admin_user_email,
        password=admin_user_password)
