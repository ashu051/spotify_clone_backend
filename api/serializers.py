from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser,User_Liked_Songs,Artist,Album,Playlist,Podcast,Premium,Song

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'country', 'password','user_profile_image','user_id']
        extra_kwargs = {'password': {'write_only': True}}
        
class User_Liked_SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Liked_Songs
        fields = '__all__'
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = '__all__'
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'