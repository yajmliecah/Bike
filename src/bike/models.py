from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from django.conf import settings
from django.db.models import Count, permalink
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from geo.models import Country, City

def get_display(key, list):
    d = dict(list)
    if key in d:
        return d[key]
    return None


class Category(models.Model):
    CATEGORY = (
        ('Cars', 'Cars'),
        ('Motorcycles', 'Motorcycles'),
        ('Vehicles', 'Vehicles')
    )
    name = models.CharField(max_length=50, choices=CATEGORY, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug, 'pk': self.id })
    @property
    def items(self):
        return Item.objects.filter(category__in=[self]).order_by("name")

    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
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

    def get_absolute_url(self):
        return reverse('brands', kwargs={'slug': self.slug })

    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)

    @classmethod
    def get_brands(cls):
        brands = list(
            cls.objects.filter(is_active=True)
        )
        return brands

    @property
    def items(self):
        return Item.objects.filter(category__in=[self]).order_by("name")


class Edition(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, null=True, blank=True)
    brand = models.ManyToManyField(Brand, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Edition")
        ordering = ['-name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('editions', kwargs={'slug': self.slug})

    def get_breadcrumbs(self):
        return ({'name': self.name, 'url': self.get_absolute_url()},)

    @classmethod
    def get_edition(cls):
        edition = list(
            cls.objects.filter(is_active=True)
        )
        return edition

    @property
    def items(self):
        return Item.objects.filter(category__in=[self]).order_by("name")


class ItemQueryset(models.query.QuerySet):

    def get_cars(self):
        return self.filter(category__name__icontains='Cars')

    def get_motorcycles(self):
        return self.filter(category__name__icontains='Motorcycles')

    def get_vehicles(self):
        return self.filter(category__name__icontains='Vehicles')

    def new(self):
        return self.filter(condition='NEW')

    def old(self):
        return self.filter(condition='OLD')


class ItemManager(models.Manager):

    def get_queryset(self):
        return ItemQueryset(self.model, using=self._db)

    def get_cars(self):
        return self.get_queryset().get_cars()

    def get_motorcycles(self):
        return self.get_queryset().get_motorcycles()

    def get_vehicles(self):
        return self.get_queryset().get_vehicles()

    def new(self):
        return self.get_queryset().new()

    def old(self):
        return self.get_queryset().old()


class Item(models.Model):
    CONDITION = (
        ('NEW', 'New'),
        ('OLD', 'Old')
    )
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    slug = models.SlugField(max_length=50, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    edition = models.ForeignKey(Edition, verbose_name=_("Edition"))
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    company = models.CharField(max_length=50, default='', verbose_name=_("Company"))
    condition = models.CharField(max_length=50, choices=CONDITION, verbose_name=_("Condition"))
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    submitted_on = models.DateField(auto_now=True, editable=False, verbose_name=_("Submitted on"))
    locations = models.ForeignKey(City, verbose_name=_("Locations"))
    active = models.BooleanField(default=True)

    objects = ItemManager()

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

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.slug})

    def get_breadcrumbs(self):
        breadcrumbs = ({'name': self.name, 'url': self.get_absolute_url()},)
        return breadcrumbs

    @classmethod
    def featured_car(cls):
        return cls.objects.all().filter(category__name__icontains='Cars')

    @classmethod
    def get_items(cls):
        return list(cls.objects.all())

    @classmethod
    def new(cls):
        return cls.objects.all().filter(condition='NEW')

    @classmethod
    def old(cls):
        return cls.objects.all().filter(condition='OLD')

    @property
    def get_conditions(self):
        return dict(Item.CONDITION)[self.condition]
