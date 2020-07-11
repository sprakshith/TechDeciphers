from django.shortcuts import render
from TechDeciphers_Leaks.models import Leaks

# def index(request):
#     return render(request, 'TechDeciphers_Leaks/leaks.html', {'times' : list(range(4))})

def index(request):
    leaksList = Leaks.objects.all().order_by('-postPublishDate')
    leaksDictionary = {'leaksList' : leaksList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_Leaks/leaksView.html', leaksDictionary)

# def leaksView(request):
#     leaksList = Leaks.objects.all().order_by('-postPublishDate')
#     leaksDictionary = {'leaksList' : leaksList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_Leaks/leaksView.html', leaksDictionary)

def leaksArticlePost(request):
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', {'times' : list(range(4))})
