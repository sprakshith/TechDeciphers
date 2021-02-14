"""TechDeciphers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from Home import views as home_views
from django.urls import path, include
from django.conf.urls.static import static
from Tutorials import views as tutorial_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('my_notebooks/', include('Notebooks.urls')),
    path('tutorials/', include('Tutorials.urls')),
    path('get_searched_article_content/', home_views.get_searched_article_content, name='get_searched_article_content'),
    path('get_searched_article_content/get_article_contents/', tutorial_views.get_article_contents, name='get_article_contents')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
