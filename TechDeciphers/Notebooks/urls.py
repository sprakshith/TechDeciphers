from django.urls import path, include
from Notebooks import views

app_name = 'Notebooks'

urlpatterns = [
    path('', views.index, name='index')
]
