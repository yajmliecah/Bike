from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy


class Category(models.Model):
    CATEGORY = (
        ('CAR', 'Car'),
        ('MOTORCYCLE', 'MotorCycle'),
        ('VEHICLE', 'Vehicle')
    )
    name = models.CharField(max_length=50, primary_key=True, choices=CATEGORY, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name

    
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
    
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)
    
    def negotiable(self):
        return self.get_queryset().negotiable()
    
    
class Item(models.Model):
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
    category = models.ForeignKey(Category, verbose_name=_("Category"))
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
    
    objects = ItemManager()
    
    class Meta:
        verbose_name = _("Item")
        ordering = ['-submitted_on']

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})

     
    