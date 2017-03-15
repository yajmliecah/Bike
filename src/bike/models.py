from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Count, permalink
from django.utils.translation import ugettext_lazy as _
from geo.models import Region, Country

    
class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Brand")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name

    
class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Edition")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    

class ItemQuerySet(models.query.QuerySet):
    
    def negotiable(self):
        return self.filter(negotiable=True)
    

class ItemManager(models.Manager):
    
 
    def negotiable(self):
        return self.get_queryset().negotiable()
    
    def featured_items(self):
        return self.all().order_by('-submitted_on')
        
    
    
class Item(models.Model):
    CATEGORY = (
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycles'),
        ('Vehicle', 'Vehicle')
    )
    CONDITION = (
        ('NEW', 'New'),
        ('OLD', 'Old')
    )
    SELLER_TYPE = (
        ('DEALER', 'Dealer'),
        ('PRIVATE', 'Private')
    )
    FUEL = (
        ('DIESEL', 'Diesel'),
        ('ELECTRO', 'Electro'),
        ('GASOLINE', 'Gasoline')
    )
    TRANS = (
        ('AUTOMATIC', 'Automatic'),
        ('MANUAL', 'Manual')
    )
    LIFESTYLES = (
        ('FAMILY', 'Family'),
        ('LUXURY', 'Luxury'),
        ('OFFROAD', 'Offroad'),
        ('CLASSIC', 'Classic')
    )
    COLOR_FAMILY = (
        ('WHITE', 'White'),
        ('BLACK', 'Black'),
    )
    NEGO = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name=_("Name"))
    image = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.IntegerField(default=0)
    negotiable = models.CharField(max_length=50, choices=NEGO)
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name=_("Condition"))
    seller_type = models.CharField(max_length=50, choices=SELLER_TYPE, verbose_name=_("Seller Type"))
    fuel = models.CharField(max_length=50, choices=FUEL, verbose_name=_("Fuel"))
    transmission = models.CharField(max_length=50, choices=TRANS, verbose_name=_("Transmission"))
    lifestyle = models.CharField(max_length=50, choices=LIFESTYLES, verbose_name=_("Lifestyle"))
    color_family = models.CharField(max_length=50, choices=COLOR_FAMILY, verbose_name=_("Color Family"))
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    submitted_on = models.DateField(auto_now=True, editable=False, verbose_name=_("Submitted on"))
    locations = models.ForeignKey(Region, blank=True, null=True, verbose_name=_("Locations"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    
    objects = ItemManager()
    
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
