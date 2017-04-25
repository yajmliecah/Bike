from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Count, permalink
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from geo.models import Country, City


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _("Category")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    
    @classmethod
    def get_category(cls):
        return list(cls.objects.all())
      
    
class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    logo = models.ImageField(blank=True, null=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = _("Brand")
        ordering = ['-name']
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    
    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)
    
    @classmethod
    def get_brand(cls):
        return list(cls.objects.all())
        
        
class Edition(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    
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
    CONDITION = (
        ('NEW', 'New'),
        ('OLD', 'Old')
    )
    name = models.CharField(max_length=100, primary_key=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True, verbose_name=_("Name"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.IntegerField(default=0)
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
        return reverse("item_detail", kwargs={"slug": self.slug})
    
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
    def new(cls):
        return cls.objects.all().filter(condition='NEW')
    
    @classmethod
    def old(cls):
        return cls.objects.all().filter(condition='OLD')