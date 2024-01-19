from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['logo', 'name', 'url']
    prepopulated_fields = {'slug': ('name', )}

    def logo(self, obj):
        if obj.logo:
            return format_html(
                "<img src='%s' />" % obj.logo.url
            )
        return '-'
    logo.short_description = "Logo"


@admin.register(WorkCategory)
class WorkCategAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'client', 'created']
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ['created']


@admin.register(TechTool)
class TechAdmin(admin.ModelAdmin):
    list_display = ['name']
