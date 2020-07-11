from django.shortcuts import render
from TechDeciphers_TopX.models import TopX

# def index(request):
#     return render(request, "TechDeciphers_TopX/topX.html", {'times' : list(range(4)), 'times2' : list(range(8))})

def index(request):
    topXList = TopX.objects.all().order_by('-postPublishDate')
    topXDictionary = {'topXList' : topXList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_TopX/topXView.html', topXDictionary)

# def topXView(request):
#     topXList = TopX.objects.all().order_by('-postPublishDate')
#     topXDictionary = {'topXList' : topXList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_TopX/topXView.html', topXDictionary)

def topXArticlePost(request):
    return render(request, "CommonTemplates/ArticlePost/articlePost.html", {'times' : list(range(4))})
