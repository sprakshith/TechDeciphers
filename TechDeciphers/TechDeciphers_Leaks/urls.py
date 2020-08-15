from django.urls import path, include
from TechDeciphers_Leaks import views
from TechDeciphers_Home import views as homeView

app_name = 'TechDeciphers_Leaks'

urlpatterns = [
    path('', views.index, name='index'),
    path('leaksForm/', views.leaksForm, name='leaksForm'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents'),
]
