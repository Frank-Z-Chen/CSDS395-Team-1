from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.template.defaultfilters import slugify, title
from django.urls import reverse
# Create your models here.

class PublicationManager(models.Manager):
    def get_query(self):
        return super(PublicationManager, self).get_queryset().filter(is_published = True)

class Wiki_page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False, verbose_name="Published?")
    create_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    publish_manager = PublicationManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Wiki_page, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('wiki_page_detail', args=(self.slug,))

class EditSession(models.Model):
    page = models.ForeignKey(Wiki_page, on_delete=CASCADE)
    edited_on = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=100)

    class Meta:
        ordering = ['-edited_on']

    def __unicode__(self):
        return "%s - %s -%s" %(self.note, self.editor, self.edited_on)

    def get_absolute_url(self):
        return reverse('edit_session_detail', args = (self.id,))

