from django.contrib import admin
from django.utils.html import format_html

from .models import Slider, Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def myPhoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', "myPhoto", "first_name", "role", "created_date")
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)