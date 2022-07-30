from django.urls import path, include
from Tutorials import views

app_name = 'Tutorials'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_tutorial/', views.tutorial_form, name='tutorial_form'),
    path('get_article_contents/', views.get_article_contents, name='get_article_contents'),
    path('fetch_previous_next_tutorials/', views.fetch_previous_next_tutorials, name='fetch_previous_next_tutorials')
]
