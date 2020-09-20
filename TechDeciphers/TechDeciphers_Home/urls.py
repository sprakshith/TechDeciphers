from django.urls import path, include
from TechDeciphers_Home import views

app_name = 'TechDeciphers_Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs/', views.aboutUsPage, name='aboutUsPage'),
    path('dropSuggestion/', views.dropSuggestion, name='dropSuggestion'),
    path('keepMeUpdated/', views.keepMeUpdated, name='keepMeUpdated'),
    path('errorPageNotFound/', views.error404PageNotFound, name='error404PageNotFound'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents'),
]
