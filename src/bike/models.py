from __future__ import unicode_literals
from django.db import models
from django.db.models import Count, permalink, Q
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

from .utils import sku_code

from geo.models import Country, City


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = _('Sub Category')

    def __unicode__(self):
        return self.name

    def get_slug(self):
        return self.slug


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    sub_category = models.ManyToManyField(SubCategory, blank=True, verbose_name=_("Sub Category"))
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = _('Category')
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_slug(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})

    def get_sub_category(self):
      return self.sub_category.all()

    @classmethod
    def get_categories(cls):
        return list(cls.objects.all())

    @classmethod
    def top_categories(cls):
        return cls.objects.annotate(score=Count('name')).order_by('score')


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
        verbose_name_plural = _('Brand')
        ordering = ['-name']

    def __unicode__(self):
        return self.name

    def get_slug(self):
        return self.slug

    def get_category(self):
        return self.category.all()

    def get_absolute_url(self):
        return reverse('brands', kwargs={'slug': self.slug, 'pk': self.pk })

    @classmethod
    def top_brands(cls):
        return cls.objects.annotate(score=Count('name')).order_by('score')

    @classmethod
    def get_brands(cls):
      return list(cls.objects.filter(is_active=True))

    @property
    def items_brand(self):
        return Item.objects.filter(category__in=[self]).order_by('name')


class ItemQueryset(models.query.QuerySet):

    def new(self):
        return self.filter(condition='NEW')

    def old(self):
        return self.filter(condition='OLD')


class ItemManager(models.Manager):

    def get_queryset(self):
        return ItemQueryset(self.model, using=self._db)

    def new(self):
        return self.get_queryset().new()

    def old(self):
        return self.get_queryset().old()


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    slug = models.SlugField(max_length=100, unique=True)
    sku = models.CharField(max_length=100, verbose_name=_("SKU"), blank=True, null=True)
    details = models.TextField(blank=True, null=True, verbose_name=_("Details"))
    short_desc = models.CharField(max_length=350, null=False, blank=False, default='Shortened Description for Product',
                                  verbose_name=_('Short Description'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    sub_category = models.ManyToManyField(SubCategory, verbose_name=_('Sub Category'))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    brand = models.ForeignKey(Brand, verbose_name=_("Brand"))
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    stock = models.IntegerField(help_text="Stock Quantity", null=True)
    view = models.BooleanField(default=0)
    company = models.CharField(max_length=50, default='', verbose_name=_("Company"))
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

        if self.sku is None or self.sku == "":
            self.sku = sku_code()
        super(Item, self).save()

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.slug})

    def get_slug(self):
        return self.slug

    def get_sub_category(self):
        return self.sub_category.all()

    def top_items(self):
        return self.objects.all()[:5]

    def get_category(self):
        return self.category.all()

    @classmethod
    def category_items(cls, category):
        return cls.objects.filter(category=category).order_by('submitted_on')

    @classmethod
    def brand_items(cls, brand):
        return cls.objects.filter(brand=brand).order_by('submitted_on')
