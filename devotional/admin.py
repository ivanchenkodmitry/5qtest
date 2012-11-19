from devotional.models import Devotional
from django.contrib import admin


class DevotionalAdmin(admin.ModelAdmin):
    list_display = ['title', 'month', 'day', 'body']


admin.site.register(Devotional, DevotionalAdmin)