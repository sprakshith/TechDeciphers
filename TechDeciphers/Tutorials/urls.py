from django.urls import path, include
from Tutorials import views

app_name = 'Tutorials'

urlpatterns = [
    path('', views.index, name='index'),
]
