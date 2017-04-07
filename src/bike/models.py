from __future__ import unicode_literals
from django.db import models
from django.conf import settings
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

        
class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("Edition")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    

class ItemQuerySet(models.query.QuerySet):
    
    def get_motorcycle(self):
        return self.filter(category='Motorcycle')
    
    def get_car(self):
        return self.filter(category='Car').order_by('-submitted_on')
    
    def get_vehicle(self):
        return self.filter(category='Vehicle')
    
    def negotiable(self):
        return self.filter(negotiable=True)
    

class ItemManager(models.Manager):
    
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)
    
    def featured_items(self):
        return self.all().order_by('-submitted_on')[:8]
        
    def get_motorcycle(self):
        return self.get_queryset().get_motorcycle()
    
    def get_car(self):
        return self.get_queryset().get_car()

    def get_vehicle(self):
        return self.get_queryset().get_vehicle()
    
    def negotiable(self):
        return self.get_queryset().negotiable()
    
    def by(self, owner):
        return self.filter(owner=owner)
    
    
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