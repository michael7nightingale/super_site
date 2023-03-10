from django.contrib import admin
from .models import *


@admin.register(CategoryMathem)
class CategoryMathemAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', )
    list_display_links = ('id', 'category_name',)
    search_field = ('category_name', )


@admin.register(Mathem)
class MathemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'exist', 'cat')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content', 'cat')
