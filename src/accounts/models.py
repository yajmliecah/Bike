from django.db import models
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from geo.models import Country, Region


class BikeUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        
        now = timezone.now()

        if not email:
            raise ValueError('Email must be set')
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        return self.create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
       return self.create_user(email, password, True, True, **extra_fields)


class BikeUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, unique=True)
    location = models.ForeignKey(Region, max_length=100)
    avatar = models.ImageField(blank=True, null=True)
    
    objects = BikeUserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['location', 'avatar']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)