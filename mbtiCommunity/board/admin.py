import imp
from django.contrib import admin
from .models import board
from django.contrib.auth.models import User

# Register your models here.
@admin.register(board)
class boardAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','published_date']
    list_display_links = ['id','title']
    list_per_page = 10
