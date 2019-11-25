from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cast(models.Model):
    # cast_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    
class Movie(models.Model):
    title = models.CharField(max_length=30)
    overview = models.TextField()
    vote_average = models.IntegerField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    trailer = models.CharField(max_length=50, blank=True, null=True)
    cast = models.ManyToManyField(Cast, related_name='cast', blank=True)
    director = models.CharField(max_length=30, blank=True)


    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']
