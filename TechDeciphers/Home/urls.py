from django.urls import path, include
from Home import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUsPage, name='aboutUsPage'),
    path('dropSuggestion/', views.dropSuggestion, name='dropSuggestion'),
    path('keepMeUpdated/', views.keepMeUpdated, name='keepMeUpdated'),
    path('get_article_post_contents/', views.get_article_contents, name='get_article_contents'),
]
