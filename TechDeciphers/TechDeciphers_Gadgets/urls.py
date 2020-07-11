from django.urls import path, include
from TechDeciphers_Gadgets import views

app_name = 'TechDeciphers_Gadgets'

urlpatterns = [
    path('', views.index, name='index'),
    # path('gadgetsTry/', views.gadgetsTry, name='gadgetsTry'),
    path('gadgetsForm/', views.gadgetsForm, name='gadgetsForm'),
    path('gadgetsArticlePost/', views.gadgetsArticlePost, name='gadgetsArticlePost')
]
