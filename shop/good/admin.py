from django.contrib import admin
from . import models

@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['t_name']

@admin.register(models.Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['g_name', 'price', 'g_type']