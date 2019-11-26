from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('index/', views.index, name='index'),
    path('index/create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/reviews/new/', views.review_create, name='new'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
]
