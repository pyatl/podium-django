from django import forms

from .models import Talk


class TalkSubmissionForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = [
            'speaker_name',
            'speaker_email',
            'title',
            'description',
            'sessions_available',
        ]
        labels = {
            'speaker_name': 'Your Name',
            'speaker_email': 'Your Email Address',
            'sessions_available': 'Dates Available to Speak',
        }
