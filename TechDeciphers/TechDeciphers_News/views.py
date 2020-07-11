from django.shortcuts import render
from TechDeciphers_News.models import News

# def index(request):
#     return render(request, 'TechDeciphers_News/news.html', {'times' : list(range(4))})

def index(request):
    newsList = News.objects.all().order_by('-postPublishDate')
    newsDictionary = {'newsList' : newsList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_News/newsView.html', newsDictionary)

# def newsView(request):
#     newsList = News.objects.all().order_by('-postPublishDate')
#     newsDictionary = {'newsList' : newsList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_News/newsView.html', newsDictionary)

def newsArticlePost(request):
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', {'times' : list(range(4))})
