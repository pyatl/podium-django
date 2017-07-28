from django.db import models


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
    description = models.TextField()
    sessions_available = models.ManyToManyField(
        'Session', related_name='talks_available')
    status = models.CharField(
        max_length=1, choices=TALK_STATUS_CHOICES,
        default='S')


class Session(models.Model):
    date = models.DateField()
    description = models.TextField(
        blank=True, help_text='Any special theme or info about the session.')

    def approved_talks(self):
        sets = [
            self.talks_available.filter(status=status) for status in ('A', 'C')
        ]
        return sets[0].union(sets[1])
