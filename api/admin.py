from django.contrib import admin
from django.apps import apps
from .models import CustomUser,User_Liked_Songs,Artist,Album,Playlist,Podcast,Premium,Song
admin.site.register((CustomUser,User_Liked_Songs,Artist,Album,Playlist,Podcast,Premium,Song))

