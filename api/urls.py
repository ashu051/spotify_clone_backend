from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api import views
router.register('register',views.RegisterViewSet,basename='resgis')
router.register('user_like_song',views.UserLikeSongViewSet,basename='user_like_song')
router.register('artist',views.ArtistViewSet,basename='artist')
router.register('album',views.AlbumViewSet,basename='album')
router.register('playlist',views.PlaylistViewSet,basename='playlist')
router.register('podcast',views.PodcastViewSet,basename='podcast')
router.register('premium',views.PremiumViewSet,basename='premium')
router.register('song',views.SongViewSet,basename='song')
urlpatterns = [
path('',include(router.urls)),
]