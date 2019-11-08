from django.contrib import admin
from pyatl.models import Location, Event, Page


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'start', 'location')


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('name', 'title')


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
