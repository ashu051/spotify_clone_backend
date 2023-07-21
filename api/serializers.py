from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser,Artist,Album,Playlist,Podcast,Premium,Song
# class User_Liked_SongsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_Liked_Songs
#         fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    # song = User_Liked_SongsSerializer(many=True, read_only=True,source='likeduser')
    # print(song)
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
# Album with artist    
class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
class AlbumArtistSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Album
        fields = '__all__'
# Album with song
class SongSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__' 
class AlbumSongSerializer(serializers.ModelSerializer):
    album = SongSerializer2(many=True,read_only=True,source='songs')
    class Meta:
        model = Album
        fields = '__all__'       
#Album Alone
class AlbumOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' 
        
        
# Song 
class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True,read_only=True)
    liked_by = serializers.SerializerMethodField()
    class Meta:
        model = Song
        fields = '__all__' 
    def get_liked_by(self, song):
        # Retrieve the liked_by users related to the song
        liked_by_users = song.liked_by.all()

        # Serialize the user data using RegistrationSerializer
        liked_by_users_data = RegistrationSerializer(liked_by_users, many=True).data

        return liked_by_users_data


# Artist Alone
class ArtistOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
# Artist with Song
class SongTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
class ArtistSongSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    class Meta:
        model = Artist
        fields = ('id', 'artist_name', 'artist_bio', 'songs')

    def get_songs(self, obj):
        # Retrieve all the songs associated with the artist
        songs = obj.song_set.all()
        # Serialize the songs using the SongSerializer
        serializer = SongSerializer(songs, many=True)
        return serializer.data



#Song Serializer
class SongOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
class SongDetailsSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True,read_only=True)
    liked_by = serializers.SerializerMethodField()
    class Meta:
        model = Song
        fields = '__all__' 
    def get_liked_by(self, song):
        # Retrieve the liked_by users related to the song
        liked_by_users = song.liked_by.all()
        # Serialize the user data using RegistrationSerializer
        liked_by_users_data = RegistrationSerializer(liked_by_users, many=True).data
        return liked_by_users_data      
        
       
# Playlist Things 
class PlaylistOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
             
class PlaylistSongSerializer(serializers.ModelSerializer):
    user = RegistrationSerializer(many=True)
    song = SongSerializer(many=True)
    class Meta:
        model = Playlist
        fields = '__all__'
        
    
# Podcast Things
class PodcastOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
        
class PodcastArtistSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    class Meta:
        model = Podcast
        fields = '__all__'



# Premium Details
class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = '__all__'
class PremiumDetailsSerializer(serializers.ModelSerializer):
    user  = RegistrationSerializer(read_only=True)
    class Meta:
        model = Premium
        fields = '__all__'
class PremiumOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = '__all__'




class MainRegister(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields=['phone_number','password']
    def create(self,validated_data):
        user = CustomUser.objects.create(phone_number=validated_data['phone_number'],
                                         )
        print(user)
        password=validated_data['password']
        print('-------------------------------------------------------')
        user.set_password(password)
        user.save()
        print('!!!!!!!!!!!!!!!!!')
        print(user)
        return user