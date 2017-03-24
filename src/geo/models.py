from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_('Name'))
    slug = models.SlugField(blank=True, null=True, verbose_name=_('Name'))
    
    class Meta:
        verbose_name = _('Country')
        verbose_name = _('Countrie')
        ordering = ['-name']
        
    def __unicode__(self):
        return self.name
     
     
class City(models.Model):
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_('Name'))
    slug = models.SlugField(blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'))
    
    class Meta:
        verbose_name = _('City')
        verbose_name = _('Citie')
        ordering = ['-name']
        app_label = 'geo'
        db_table = 'geo'
        
    def __unicode__(self):
        return self.name