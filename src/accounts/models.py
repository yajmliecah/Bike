from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True)
    membership =models.DateField(auto_now=True, editable=False)
    mobile_number = models.IntegerField(default=0)

    class Meta:
        db_table = 'auth_profile'
        
    def __unicode__(self):
        return self.user.username
    

    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', (), {'pk': self.pk})
