from django.urls import path, include
from TechDeciphers_News import views
from TechDeciphers_Home import views as homeView

app_name = 'TechDeciphers_News'


urlpatterns = [
    path('', views.index, name='index'),
    # path('tryingAjaxCall/', views.tryingAjaxCall, name='tryingAjaxCall'),
    path('newsForm/', views.newsForm, name='newsForm'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents')
]
