from django.contrib import admin
from .models import Movie, Review, Genre, Cast

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'vote_average',)

class CastAdmin(admin.ModelAdmin):
    list_display = ('name', 'path',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', 'score', 'user', 'movie',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Cast, CastAdmin)
