from django.contrib import admin
from .models import Talk, Session


class TalkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = ['speaker_name',
                    'speaker_email',
                    'title',
                    'short_description',
                    'status',
                    ]

    list_display_links = ['speaker_name']

    list_editable = ['status']

    list_filter = [
        'sessions_available',
        'speaker_name',
        'speaker_email',
        'title',
        'status',
    ]

    search_fields = [
        'speaker_name',
        'speaker_email',
        'title',
        'description',
        'status',
    ]

    class meta:
        model = Talk


admin.site.register(Talk, TalkAdmin)
admin.site.register(Session)
