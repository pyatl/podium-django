from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


TALK_STATUS_CHOICES = (
    ('S', 'Submitted'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
    ('C', 'Confirmed'),
)


class Talk(models.Model):
    speaker_name = models.CharField(max_length=1000)
    speaker_email = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField()
    sessions_available = models.ManyToManyField(
        'Session', related_name='talks_available')
    status = models.CharField(
        max_length=1, choices=TALK_STATUS_CHOICES,
        default='S')

    def get_absolute_url(self):
        return reverse('talks-talk-id', args=[self.slug])

    def __str__(self):
        return self.speaker_name

    @property
    def short_description(self):
        """ Return truncated description of specified length
        as a Talk field using @property decorator"""
        return truncatechars(self.description, 20)

    class meta:
        ordering = ['-id']


class Session(models.Model):
    date = models.DateField()
    description = models.TextField(
        blank=True, help_text='Any special theme or info about the session.')

    def __str__(self):

        return '{} - {} '.format(self.date, self.description)

    def approved_talks(self):
        return self.talks_available.filter(status__in=('A', 'C'))

    def get_absolute_url(self):
        return reverse('talks-sessions-id', args=[self.date])


def create_slug(instance, new_slug=None):
    """ Return slugified string to be used as
    object id in url """

    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Talk.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = '{}-{}'.format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug


# same as pre_save.connect(pre_save_talk_reciever, sender=Talk)
@receiver(pre_save, sender=Talk)
def pre_save_talk_reciever(sender, instance, *args, **kwargs):
    """ Function to be invoked before saving instance and call
    create_slug if there is no associated slug """

    if not instance.slug:
        instance.slug = create_slug(instance)
