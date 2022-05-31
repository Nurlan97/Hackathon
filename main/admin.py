from django.contrib import admin

# Register your models here.
from main.models import Song, Category

admin.site.register(Song)
admin.site.register(Category)
