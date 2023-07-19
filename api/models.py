from django.db import models

# Create your models here.


# create company model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .manager import UserManger
class CustomUser(AbstractUser):
    username = None
    user_id = models.IntegerField(primary_key=True)  
    password = models.TextField()  
    phone_number =models.TextField(unique=True)
    user_profile_image = models.ImageField(upload_to="profile")
    country = models.TextField()
    objects=UserManger()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return str(str(self.user_id) +" "+self.phone_number)
class Premium(models.Model):
    PT = (
        ("basic","Basic"),
        ("standard","Standard"),
        ("elite","Elite")
    )
    id = models.IntegerField(primary_key=True)
    premium_type = models.TextField(choices=PT,default="basic")
    premium_active = models.BooleanField(default=False) 
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return str(str(self.id) +" "+str(self.premium_active) +" "+self.premium_type)
class Artist(models.Model):
    id  = models.IntegerField(primary_key=True)
    artist_name= models.TextField()
    artist_bio = models.TextField()
    def __str__(self):
        return str(self.artist_name +" "+self.artist_bio)
class Album(models.Model):
    artist_album = models.ManyToManyField(Artist)
    id = models.IntegerField(primary_key=True)
    album_name  = models.TextField()
    def __str__(self):
        return str(str(self.id) +" "+self.album_name)
class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    playlist_name = models.TextField()
    user = models.ManyToManyField(CustomUser)
    def __str__(self):
        return str(str(self.id) +" "+self.playlist_name +" "+self.user)
class Song(models.Model):
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    artist_songs = models.ManyToManyField(Artist)
    playlist_song = models.ManyToManyField(Playlist,blank=True)
    id = models.IntegerField(primary_key=True)
    song_name=models.TextField(max_length=70)
    song_duration = models.FloatField()
    def __str__(self):
        return str(str(self.id) +" "+self.song_name +" "+self.artist_songs +" "+self.playlist_song)
class User_Liked_Songs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    def __str__(self):
        return str(str(self.id) +" "+self.user_id +" "+self.song_id)
class Podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    podcast_name = models.TextField()
    podcast_duration = models.FloatField()
    artist_podcast = models.ManyToManyField(Artist)
    def __str__(self):
        return str(str(self.id) +" "+self.podcast_duration +" "+self.podcast_name +" "+self.artist_podcast)
    
   
