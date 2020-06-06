from django.shortcuts import render

def index(request):
    return render(request, "TechDeciphers_TopX/topX.html", {'times' : list(range(4)), 'times2' : list(range(8))})

def topXArticlePost(request):
    return render(request, "CommonTemplates/ArticlePost/articlePost.html", {'times' : list(range(4))})
