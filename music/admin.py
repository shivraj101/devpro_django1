from django.contrib import admin
from .models import Album,Song
# Register your models here.

admin.site.register(Album) #gets the data from Album model into our admin panel
admin.site.register(Song)