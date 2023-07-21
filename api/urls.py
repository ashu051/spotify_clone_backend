from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api import views
# router.register('user_like_song',views.UserLikeSongViewSet,basename='user_like_song')
router.register('user',views.UserViewSet,basename='user')

router.register('verified-user',views.RegisterViewSet,basename='verified')

# artist urls
router.register('artist',views.ArtistOnlyViewSet,basename='artist')
router.register('artist-songs',views.ArtistSongViewSet,basename='artist-songs')

# common for artist and albums
router.register('album-artist',views.AlbumArtistViewSet,basename='album-artist')

#album urls
router.register('album-songs',views.AlbumSongViewSet,basename='album-song')
router.register('album',views.AlbumOnlyViewSet,basename='album-only')

# playlist urls
router.register('playlist',views.PlaylistOnlyViewSet,basename='playlist')
router.register('playlist-song',views.PlaylistSongViewSet,basename='playlist-song')
router.register('user-playlist',views.PlaylistUserViewSet,basename='user-playlist')

# podcast urls
router.register('podcast',views.PodcastOnlyViewSet,basename='podcast')
router.register('podcast-artist',views.PodcastArtistViewSet,basename='podcast-artist')


# premium urls
router.register('premium',views.PremiumViewSet,basename='premium')
router.register('premium-user',views.PremiumDetailsViewSet,basename='premium-user')


# song urls
router.register('song',views.SongOnlyViewSet,basename='song')
router.register('song-details',views.SongDetailsViewSet,basename='song-details')




# router.register('asongs',views.AlbumSongsView,basename='album-song')

urlpatterns = [
path('',include(router.urls)),
path('register/',views.RegisterUser.as_view())

]