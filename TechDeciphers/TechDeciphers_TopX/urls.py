from django.urls import path, include
from TechDeciphers_TopX import views
from TechDeciphers_Home import views as homeView

app_name = 'TechDeciphers_TopX'

urlpatterns = [
    path('', views.index, name='index'),
    path('trendingForm/', views.trendingForm, name='trendingForm'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents')
]
