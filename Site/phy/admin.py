from django.contrib import admin
from .models import *


@admin.register(CategoryPhy)
class CategoryPhyAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', )
    list_display_links = ('id', 'category_name',)
    search_field = ('category_name', )
    list_filter = ('category_name', "id")


@admin.register(Phy)
class PhyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'exist', 'cat')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content', 'cat')
    list_filter = ('title', "id")


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "content", "cat", "slug")
    list_display_links = ("id", "name", "slug")
    search_fields = ("name", "slug")
    list_filter = ('name', "id")

