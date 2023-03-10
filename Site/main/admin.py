from django.contrib import admin
from .models import *


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'exist', )
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'content', )
    list_filter = ('id', )
