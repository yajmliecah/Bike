from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('Title'))
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    content = models.TextField(max_length=3000)
    posted_on = models.DateTimeField(auto_now=True, verbose_name=_('Created on'))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    updated_by = models.CharField(max_length=55)
    
    class Meta:
        verbose_name = _('Post')
        ordering = ('posted_on',)
        
    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        from unidecode import unidecode
        from django.template import defaultfilters
        if not self.title == "":
            self.slug = defaultfilters.slugify(unidecode(self.title))
        super(Post, self).save()
        
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
    def get_comments(self):
        return Comment.objects.filter(post=self)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        verbose_name = _('Comment')
        ordering = ('date',)
        
    def __unicode__(self):
        return '{0} - {1}'.format(self.user.username, self.post.title)
  
  
class Tag(models.Model):
    title = models.CharField(max_length=50)
    post = models.ForeignKey(Post)
    
    class Meta:
        verbose_name = _('Tag')