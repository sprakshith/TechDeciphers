from django.urls import path, include
from TechDeciphers_Home import views

app_name = 'TechDeciphers_Home'

urlpatterns = [
    path('', views.index, name='index'),
]
