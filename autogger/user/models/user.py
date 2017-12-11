from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'user_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
