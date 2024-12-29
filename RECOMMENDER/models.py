
# Create your models here.
from django.db import models


# Create your models here.
# HINT: Create a Movie model here
# It will be mapped to a database table with columns
class Movie(models.Model):
   
    imdb_id = models.CharField(max_length=48, null=False)
    genres = models.CharField(max_length=200, null=True)
    original_language = models.CharField(max_length=20, null=True)
    original_title = models.CharField(max_length=500, null=False)
    release_date = models.IntegerField(default=1970)
    overview = models.TextField(max_length=2000, null=True)
    vote_average = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    poster_path = models.CharField(max_length=64, null=True)
    watched = models.BooleanField(default=False, null=True)
    recommended = models.BooleanField(default=False, null=True)
