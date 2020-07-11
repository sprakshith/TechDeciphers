from django.urls import path, include
from TechDeciphers_Leaks import views

app_name = 'TechDeciphers_Leaks'

urlpatterns = [
    path('', views.index, name='index'),
    # path('leaksView/', views.leaksView, name='leaksView'),
    path('leaksArticlePost/', views.leaksArticlePost, name='leaksArticlePost'),
]
