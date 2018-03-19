from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField() #we can enter link for logo image

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk}) #keyword arguments

    def __str__(self): #string representation of objects (built-in syntax)
        # return self.album_title + ' - '  + self.artist + ' - ' +self.genre
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE) #cascade -> delete songs when album is deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self): #string representation of objects (built-in syntax)
        return self.song_title
        # return self.song_title+'-'+self.file_type