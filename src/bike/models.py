from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _


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
        verbose_name_plural = _("Brands")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name


class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Edition")
        verbose_name_plural = _("Editions")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    
    
class Item(models.Model):
    CONDITION =(
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
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name=_("Name"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.IntegerField(default=0)
    negotiable = models.BooleanField(default=True)
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name=_("Condition"))
    seller_type = models.CharField(max_length=50, choices=SELLER_TYPE, verbose_name=_("Seller Type"))
    fuel = models.CharField(max_length=50, choices=FUEL, verbose_name=_("Fuel"))
    transmission = models.CharField(max_length=50, choices=TRANS, verbose_name=_("Transmission"))
    lifestyle = models.CharField(max_length=50, choices=LIFESTYLES, verbose_name=_("Lifestyle"))
    color_family = models.CharField(max_length=50, choices=COLOR_FAMILY, verbose_name=_("Color Family"))
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    submitted_on = models.DateField(auto_now=True, editable=False, verbose_name=_("Submitted on"))
    
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        ordering = ['-submitted_on']

    def __unicode__(self):
        return self.name
     
    