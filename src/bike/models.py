from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from django.conf import settings
from django.db.models import Count, permalink
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db.models import Q
from geo.models import Country, City


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
     
    @classmethod
    def get_category(cls):
        return list(cls.objects.filter(is_active=True))
    

class BrandManager(models.Manager):
    def top_brands(self):
        return self.annotate(score=Count('name')).order_by('-score')

      
class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    logo = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Brand")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return reverse("brand", kwargs={"slug": self.slug})
    
    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)
    
    @classmethod
    def get_brands(cls):
        brands = list(
            cls.objects.filter(is_active=True)
        )
        return brands
    
     
class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
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
        edition = list(
            cls.objects.filter(is_active=True)
        )
        return edition
    

class Item(models.Model):
    CONDITION = (
        ('NEW', 'New'),
        ('OLD', 'Old')
    )
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name=_("Name"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    brand = models.OneToOneField(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    company = models.CharField(max_length=50, default='', verbose_name=_("Company"))
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name=_("Condition"))
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    submitted_on = models.DateField(auto_now=True, editable=False, verbose_name=_("Submitted on"))
    locations = models.ForeignKey(City, verbose_name=_("Locations"))
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _("Item")
        ordering = ['-submitted_on']
        app_label = 'bike'
        db_table = 'bike'
        
    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from unidecode import unidecode
        from django.template import defaultfilters
        if not self.name == "":
            self.slug = defaultfilters.slugify(unidecode(self.name))
        super(Item, self).save()
    
    @models.permalink
    def get_absolute_url(self):
        return reverse("item", kwargs={"slug": self.slug})
    
    def get_breadcrumbs(self):
        
        breadcrumbs = ({'name': self.name, 'url': self.get_absolute_url()},)
      #  if self.parent:
       #     return self.parent.get_breadcrumb() + breadcrumbs
        return breadcrumbs
    
    @classmethod
    def get_detail(cls, pk):
        item_detail = list(
            cls.objects.get(pk=pk)
        )
        return item_detail
        
    @classmethod
    def featured_car(cls):
        return cls.objects.all().filter(category__name__icontains='Car')
    
    @classmethod
    def get_items(cls):
        return list(cls.objects.all())
    
    @classmethod
    def new(cls):
        return cls.objects.all().filter(condition='NEW')
    
    @classmethod
    def old(cls):
        return cls.objects.all().filter(condition='OLD')
    
    @classmethod
    def get_cars(cls):
        cars = list(
            cls.objects.filter(category__name__icontains='Car')
        )
        return cars

    @classmethod
    def get_motorcycles(cls):
        motorcycles = list(
            cls.objects.filter(category__name__icontains='Motorcycle')
        )
        return motorcycles
    
    @classmethod
    def get_vehicles(cls):
        vehicles = list(
            cls.objects.filter(category__name__icontains='Vehicles')
        )
        return vehicles