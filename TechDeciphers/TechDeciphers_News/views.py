from django.shortcuts import render

def index(request):
    return render(request, 'TechDeciphers_Leaks/leaks.html', {'times' : list(range(4))})

def newsArticlePost(request):
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', {'times' : list(range(4))})
