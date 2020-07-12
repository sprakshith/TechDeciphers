from django.urls import path, include
from TechDeciphers_Gadgets import views

app_name = 'TechDeciphers_Gadgets'

urlpatterns = [
    path('', views.index, name='index'),
    path('gadgetsForm/', views.gadgetsForm, name='gadgetsForm'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents')
]
