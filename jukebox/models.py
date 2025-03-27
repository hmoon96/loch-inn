from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Music_Embed(models.Model):
    """
    
    """
    embed_code = models.CharField(max_length=255, unique=True)
    genre = models.CharField(max_length=100, blank=True)
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return f"{self.song_name} by {self.artist_name}"


class Global_List(models.Model):
    """
    
    """
    embed_id = models.ForeignKey(
        Music_Embed,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    datetime_added = models.DateTimeField(auto_now_add=True)


class Local_List(models.Model):
    """
    
    """
    embed_id = models.ForeignKey(
        Music_Embed,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    datetime_added = models.DateTimeField(auto_now_add=True)


