from django.contrib import admin
from django.apps import apps
from .models import CustomUser,Artist,Album,Playlist,Podcast,Premium,Song
admin.site.register((CustomUser,Artist,Album,Playlist,Podcast,Premium,Song))

