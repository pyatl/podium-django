from django.db import models


TALK_STATUS_CHOICES = (
    ('S', 'Submitted'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
    ('C', 'Confirmed'),
)


class Talk(models.Model):

    speaker_name = models.CharField(max_length =1000)
    speaker_email = models.CharField(max_length =1000)
    title = models.CharField(max_length =1000)
    description = models.TextField()

    sessions_available = models.ManyToManyField(
                                                'Session', related_name = 'talks_available')

    status = models.CharField(
                                max_length =1, choices = TALK_STATUS_CHOICES,
                                default = 'S')

    def __str__(self):
        return self.title


class Session(models.Model):

    # date = models.DateField()
    date = models.DateField(auto_now = False , auto_now_add = False)
    description = models.TextField(
        blank=True, help_text = 'Any special theme or info about the session.')

    def __str__(self):
        return '{} - {} '.format(self.date, self.description )

    def approved_talks(self):
        return self.talks_available.filter(status = 'A')
