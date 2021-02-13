from django.urls import path, include
from Notebooks import views

app_name = 'Notebooks'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_notebook/', views.notebook_form, name='notebook_form'),
    path('get_article_contents/', views.get_article_contents, name='get_article_contents')
]
