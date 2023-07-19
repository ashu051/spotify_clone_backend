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

    
  
class Artist(models.Model):
    id  = models.IntegerField(primary_key=True)
    artist_name= models.TextField()
    artist_bio = models.TextField()
class Album(models.Model):
    artist_album = models.ManyToManyField(Artist)
    id = models.IntegerField(primary_key=True)
    album_name  = models.TextField()
class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    playlist_name = models.TextField()
    user = models.ManyToManyField(CustomUser)
class Song(models.Model):
    artist_songs = models.ManyToManyField(Artist)
    playlist_song = models.ManyToManyField(Playlist)
    id = models.IntegerField(primary_key=True)
    song_name=models.TextField(max_length=70)
    song_duration = models.FloatField()
class User_Liked_Songs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
class Podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    podcast_name = models.TextField()
    podcast_duration = models.FloatField()
    artist_podcast = models.ManyToManyField(Artist)
