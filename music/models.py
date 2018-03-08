from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000) #we can enter link for logo image

    def __str__(self): #string representation of objects (built-in syntax)
        return self.album_title + ' - '  + self.artist + ' - ' +self.genre

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE) #cascade -> delete songs when album is deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self): #string representation of objects (built-in syntax)
        return self.song_title