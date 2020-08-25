from django.urls import path, include
from TechDeciphers_ChatBotService import views

app_name = 'TechDeciphers_ChatBotService'

urlpatterns = [
    path('', views.index, name='index')
]
