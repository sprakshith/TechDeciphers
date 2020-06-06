from django.shortcuts import render

def index(request):
    return render(request, 'TechDeciphers_Gadgets/index.html', {'times' : list(range(4))})

def gadgetsArticlePost(request):
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', {'times' : list(range(4))})
