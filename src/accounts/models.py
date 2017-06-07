from datetime import timedelta

from django.db import models
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone
from geo.models import *
from bike.models import *


class BikeUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_verified=False):
        
        verify_code = None
        if not is_verified:
            verify_code = self.make_random_password(length=20)
        if not email:
            raise ValueError('Email must be set')
        if self.filter(email__iexact=email).count() > 0:
            raise ValidationError("User with this Email address already exists.")
        
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          is_verified=is_verified,
                          is_active=True,
                          )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        
        return user
     
    def create_superuser(self, username, email, password):
        user = self.create_user(username=username,
                                email=email,
                                password=password
                                )
        user.is_admin = True
        user.save(using=self._db)
        
        return user

    def get_reset_code(self, email):
        """
        Generates a new password reset code returns user
        """
    
        try:
            user = self.get(email__iexact=email)
            user.reset_code = self.make_random_password(length=20)
            user.reset_code_expire = timezone.now() + timedelta(days=2)
            user.save()
        
            return user
        except get_user_model().DoesNotExist:
            raise ValidationError('We can\'t find that email address, sorry!')

    def reset_password(self, user_id, reset_code, password):
        """
        Set new password for the user
        """
    
        if not password:
            raise ValidationError('New password can\'t be blank.')
    
        try:
            user = self.get(id=user_id)
            if not user.reset_code or user.reset_code != reset_code or user.reset_code_expire < timezone.now():
                raise ValidationError('Password reset code is invalid or expired.')
        
            # Password reset code shouldn't be used again
            user.reset_code = None
            user.set_password(password)
            user.save()
    
        except get_user_model().DoesNotExist:
            raise ValidationError('Password reset code is invalid or expired.')


class BikeUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False, unique=True)
    location = models.ForeignKey(City, max_length=100, null=True, blank=True)
    is_verified = models.CharField(max_length=512, blank=True, null=True,
                                   help_text='User account verification code.', editable=False)
    reset_code = models.CharField(max_length=512, blank=True, null=True,
                                  help_text='Password reset code.', editable=False)
    reset_code_expire = models.DateTimeField(max_length=512, blank=True, null=True,
                                             help_text='Password reset code expire date.', editable=False)
    avatar = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = BikeUserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def get_absolute_url(self):
        
        return reverse('profile', (), {'pk': self.pk})
    
    @classmethod
    def get_by_username(cls, username):
        
        return cls.objects.get(username__iexact=username)
    