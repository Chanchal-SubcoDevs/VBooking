from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app 
    """
    def create_user(self, email, password, **extra_fileds):
        if not email:
            raise ValueError(_('The email must be set'))
        if not password:
            raise ValueError(_('The password must be set'))
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fileds)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault('is_active', True)
        extra_fileds.setdefault('role', 1)

        if extra_fileds.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin.')
        return self.create_user(email, password, **extra_fileds)