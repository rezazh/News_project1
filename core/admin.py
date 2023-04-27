from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ['title','categories']
    list_per_page = 10
    search_fields = ['title']
    list_filter = ['created_at', 'last_update']