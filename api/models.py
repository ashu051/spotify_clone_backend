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
    premium_type = models.TextField(choices=PT,default="basic")
    premium_active = models.BooleanField(default=False) 
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='premium')
    def __str__(self):
        return str(str(self.id) +" "+str(self.premium_active) +" "+self.premium_type)
class Artist(models.Model):
    artist_name= models.TextField()
    artist_bio = models.TextField()
    def __str__(self):
        return str(self.artist_name +" "+self.artist_bio)
class Album(models.Model):
    artist = models.ManyToManyField(Artist,related_name='albums')
    album_name  = models.TextField()
    def __str__(self):
        return str(str(self.id) +" "+self.album_name)
    
class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name='songs')
    artist = models.ManyToManyField(Artist)
    song_name=models.TextField(max_length=70)
    song_duration = models.FloatField()
    liked_by  = models.ManyToManyField(CustomUser)
    def __str__(self):
        return str(str(self.id) +" "+self.song_name )
class Playlist(models.Model):
    playlist_name = models.TextField()
    user = models.ManyToManyField(CustomUser)
    song = models.ManyToManyField(Song,blank=True)
    def __str__(self):
        return str(str(self.id) +" "+self.playlist_name +" "+self.user)

# class User_Liked_Songs(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='likeduser')
#     song_id = models.ForeignKey(Song,on_delete=models.CASCADE,related_name='likedsongs')
#     def __str__(self):
#         return str(str(self.id) +" "+self.user_id +" "+self.song_id)
class Podcast(models.Model):
    podcast_name = models.TextField()
    podcast_duration = models.FloatField()
    artist = models.ManyToManyField(Artist)
    def __str__(self):
        return str(str(self.id) +" "+self.podcast_duration +" "+self.podcast_name +" "+self.artist)
    
   
