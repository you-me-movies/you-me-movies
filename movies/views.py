from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .models import Movie, Review, Genre
from .forms import ReviewForm, MovieForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic.detail import SingleObjectMixin
from IPython import embed

# Create your views here.
def first_page(request):
    # if request.user.is_authenticated:
    scores = request.user.review_set.filter(score__gte=5).order_by('-score').values('genres_id')
    context = {'scores': scores}
    return render(request, 'movies/first_page.html', context)
    # else:
    #     return redirect('movies:first_page')


def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {'movies': movies, 'genres': genres,}
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movie.review_set.all()
    
    context = {'movie': movie, 'reviews': reviews, 'review_form': review_form}
    return render(request, 'movies/detail.html', context)


@require_POST
def review_create(request, movie_pk):
    if request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        genres = Movie.objects.filter(pk=movie_pk).values('genre_ids')[0]
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie_id = movie_pk
            review.genres_id = genres['genre_ids']
            review.user = request.user
            review.save()

    return redirect('movies:detail', movie_pk)


@require_POST
def review_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
        return redirect('movies:detail', movie_pk)
    return HttpResponse('작성한 댓글이 아닙니다.', status=401)


@login_required
def review_update(request, review_pk):
    if request.method == 'POST':
        review = ReviewForm(request.POST, instance=request.user)
        if review.is_valid():
            review.save()
            return redirect('movies:detail')
    else:
        review = ReviewForm(instance=request.user)
    context = {'review': review,}
    return render(request, 'movies/detail.html', context)   


@login_required
def like(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {'liked': liked, 'count': movie.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()


@staff_member_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()                
        return redirect('movies:index')         
    else:
        form = MovieForm()
    context = {'form': form,}
    return render(request, 'movies/form.html', context)


@staff_member_required
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_staff:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                movie.save()
                return redirect('movies:detail', movie_pk)
        else:

            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie_pk)
    context = {'form': form, 'movie': movie,}
    return render(request, 'movies/form.html', context)


@login_required
def recommend(request):
    # print(request.user.user_set.all())
    if request.user.is_authenticated:
        # movie_ids = request.user.review_set.filter(score__gte=5).values('movie_id')[:5]
        scores = request.user.review_set.filter(score__gte=5).order_by('-score').values('genres_id')
        if scores.count():
            movies = Movie.objects.filter(genre_ids=scores[0].get('genres_id'))[:10]
        # genres = {}
        # for score in scores:
        #     if score.get('movie_id') in movies.all():
        #         genres[score.get('movie_id')].add(score.get('genre_ids'))
                

            context = {'scores': scores, 'movies': movies}
            return render(request, 'movies/recommend.html', context)    
        else:
            return redirect('movies:index')
    else:
        # user = request.user
        # review = get_object_or_404(Review)
        # context = {'review': review,}
        # return render(request, 'movies:index', context)
        return redirect('movies:index')
