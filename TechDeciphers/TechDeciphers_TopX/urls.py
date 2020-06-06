from django.urls import path, include
from TechDeciphers_TopX import views

app_name = 'TechDeciphers_TopX'

urlpatterns = [
    path('', views.index, name='index'),
    path('topXArticlePost/', views.topXArticlePost, name='topXArticlePost'),
]
