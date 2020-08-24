from django.urls import path, include
from TechDeciphers_Home import views

app_name = 'TechDeciphers_Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('errorPageNotFound/', views.error404PageNotFound, name='error404PageNotFound'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents'),
    path('sms/', views.sms, name='sms')
]
