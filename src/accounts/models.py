from django.db import models
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from geo.models import *
from bike.models import *


class BikeUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        
        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=self.normalize_email(email),
                          username=username,
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


class BikeUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False, unique=True)
    location = models.ForeignKey(City, max_length=100, null=True, blank=True)
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