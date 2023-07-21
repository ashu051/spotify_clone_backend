from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
# class UserLikeSongViewSet(viewsets.ModelViewSet):
#     queryset = User_Liked_Songs.objects.all()
#     serializer_class =User_Liked_SongsSerializer
class RegisterUser(APIView):
    def post(self,request):
        serializer = MainRegister(data = request.data)
        print(request.data)
        if not serializer.is_valid():
            print('***************************')
            print(serializer.errors)
            return Response({"insecure":serializer.errors}) 
        print('############################')
        serializer.save()
        # print(serializer.data)
        user = CustomUser.objects.get(phone_number=serializer.data['phone_number'])
        token_obj,_ = Token.objects.get_or_create(user =user)
        return Response(serializer.data, status=status.HTTP_200_OK) 

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated        
    


# Premium things
class PremiumViewSet(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiumOnlySerializer
    def create(self, request, *args, **kwargs):
        # Check if a premium entry already exists for the user
        user = request.data.get('user')
        if Premium.objects.filter(user=user).exists():
            return Response({"error": "User already has a premium entry."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        premium = self.get_object()
        # Partially update the song with the data from the request
        serializer = self.get_serializer(premium, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
class PremiumDetailsViewSet(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class = PremiumDetailsSerializer

    # def get_queryset(self):
    #     # Filter playlists by the current authenticated user
    #     user = self.request.user
    #     return Premium.objects.filter(user=user)
    
    
    
#Artist Things
class ArtistOnlyViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistOnlySerializer
class ArtistSongViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSongSerializer



#Playlist Things
class PodcastOnlyViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastOnlySerializer

class PodcastArtistViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastArtistSerializer


 #Playlist Things
class PlaylistOnlyViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistOnlySerializer
class PlaylistSongViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSongSerializer
class PlaylistUserViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistOnlySerializer
    def get_queryset(self):
        # Filter playlists by the current authenticated user
        user = self.request.user
        return Playlist.objects.filter(user=user)
 
 
 
# ALBUM Things
class AlbumSongViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSongSerializer      
class AlbumOnlyViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    print(queryset)
    serializer_class = AlbumOnlySerializer      
class AlbumArtistViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumArtistSerializer  
 # Song Detail
class SongOnlyViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongOnlySerializer 
    def patch(self, request, *args, **kwargs):
        song = self.get_object()
        # Partially update the song with the data from the request
        serializer = self.get_serializer(song, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
class SongDetailsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongDetailsSerializer  


