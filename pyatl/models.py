from django.db import models
from tinymce import models as tinymce_models


class Location(models.Model):
    '''
    Defines an event's location.
    For physycal locations it allows 
    for optional open street maps embed codes.
    This is an iframe embed code provided 
    in the open street maps website.

    For online locations, simply leave the map_embed_code 
    field blank and include a link to the online room
    in the description.
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = tinymce_models.HTMLField() # wysiwyg
    map_embed_code = models.TextField(blank=True) # open street map embed code

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    '''
    Defines a group event.
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    short_description = models.TextField(max_length=280) # size of tweet
    description = tinymce_models.HTMLField() # wysiwyg
    date = models.DateTimeField()
    published = models.BooleanField(default=False)
    location = models.ForeignKey('Location', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    @property
    def slugify_date(self):
        return self.date.strftime('%Y-%m-%d')
    
    class Meta:
        ordering = ['date']


class Page(models.Model):
    '''
    Defines a generic content page.
    Meant for content like the Code of Conduct.

    Field footer_link defines if a link to this page 
    should be included in the footer area.
    '''
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = tinymce_models.HTMLField() # wysiwyg
    published = models.BooleanField(default=False)
    footer_link = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']