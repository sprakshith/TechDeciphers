from django.urls import path, include
from TechDeciphers_News import views

app_name = 'TechDeciphers_News'


urlpatterns = [
    path('', views.index, name='index'),
    # path('tryingAjaxCall/', views.tryingAjaxCall, name='tryingAjaxCall'),
    path('getArticlePostContents/', views.getArticlePostContents, name='getArticlePostContents')
]
