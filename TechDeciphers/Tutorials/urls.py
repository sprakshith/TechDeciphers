from django.urls import path, include
from Tutorials import views

app_name = 'Tutorials'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_tutorial/', views.tutorial_form, name='tutorial_form')
]
