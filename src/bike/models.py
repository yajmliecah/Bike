from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Count, permalink
from django.utils.translation import ugettext_lazy as _
from geo.models import Country, City

    
class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Brand")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('brand', (), {'pk': self.pk})
    
    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)
    
    @classmethod
    def get_brand(cls):
        return list(cls.objects.all())
        
        
class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Edition")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('edition', (), {'pk': self.pk})
    
    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)
    
    @classmethod
    def get_edition(cls):
        return list(cls.objects.all())
    
    
class Item(models.Model):
    CATEGORY = (
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Vehicle', 'Vehicle')
    )
    CONDITION = (
        ('NEW', 'New'),
        ('OLD', 'Old')
    )
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name=_("Name"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.IntegerField(default=0)
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name=_("Condition"))
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    submitted_on = models.DateField(auto_now=True, editable=False, verbose_name=_("Submitted on"))
    locations = models.ForeignKey(City, verbose_name=_("Locations"))
    
    class Meta:
        verbose_name = _("Item")
        ordering = ['-submitted_on']
        app_label = 'bike'
        db_table = 'bike'
        
    def __unicode__(self):
        return self.category + ' - ' + self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('item_detail', (), {'pk': self.pk})
    
    def get_breadcrumbs(self):
        
        breadcrumbs = ({'name': self.name, 'url': self.get_absolute_url()},)
        
        if self.parent:
            return self.parent.get_breadcrumb() + breadcrumbs
        
        return breadcrumbs

    @classmethod
    def featured_items(cls):
        return cls.objects.all()[:8]
    
    @classmethod
    def get_items(cls):
        return list(cls.objects.all())
    
    @classmethod
    def get_car(cls):
        return cls.objects.filter(category='Car')
    
    @classmethod
    def get_motorcycle(cls):
        return cls.objects.filter(category='Motorcycle')
    
    @classmethod
    def get_vehicle(cls):
        return cls.objects.filter(category='Vehicle')
    
    @classmethod
    def new(cls):
        return cls.objects.filter(condition='NEW')
    
    @classmethod
    def old(cls):
        return cls.objects.filter(condition='OLD')