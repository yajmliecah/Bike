from django.db import models
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from geo.models import Country, Region


class BikeUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, location, avatar, password=None):
        
        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          first_name=first_name,
                          last_name=last_name,
                          location=location,
                          avatar=avatar,
                          is_active=True,
                          )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        
        return user
     
    def create_superuser(self, username, first_name, last_name, email, location, avatar, password):
        user = self.create_user(username=username,
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                location=location,
                                avatar=avatar,
                                password=password,
                                )
        user.is_admin = True
        user.save(using=self._db)
        
        return user


class BikeUser(AbstractBaseUser):
    username = models.CharField(max_length=100, primary_key=True, db_index=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, unique=True)
    location = models.ForeignKey(Region, max_length=100)
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
        return self.email

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