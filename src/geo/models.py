from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_('Name'))
    slug = models.SlugField(blank=True, null=True, verbose_name=_('Name'))
    
    class Meta:
        verbose_name = _('Country')
        ordering = ['-name']
        
    def __unicode__(self):
        return self.name
     
     
class Region(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_('Name'))
    slug = models.SlugField(blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'))
    
    class Meta:
        verbose_name = _('Region')
        ordering = ['-name']