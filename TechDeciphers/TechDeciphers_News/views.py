from django.shortcuts import render, redirect
from TechDeciphers_News.models import News
from django.http import JsonResponse

# def index(request):
#     return render(request, 'TechDeciphers_News/news.html', {'times' : list(range(4))})

def index(request):
    newsList = News.objects.all().order_by('-postPublishDate')
    newsDictionary = {'newsList' : newsList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_News/newsView.html', newsDictionary)

# def tryingAjaxCall(request):
#     print("Came Inside Without Anyproblem, Thanks to Ajax")
#     currentArticleId = request.GET.get('primary_key', None)
#     return JsonResponse({})

def getArticlePostContents(request):
    print("Came Inside Get Article Contents");
    articleId = request.POST.get('articlePrimaryId', None)
    myArticle = News.objects.filter(newsId = articleId)[0]
    myArticleContents = {
                            'articleImage' : myArticle.newsImage,
                            'heading' : myArticle.heading,
                            'miniHeading' : myArticle.miniHeading,
                            'completeContent' : myArticle.completeContent,
                            'postAuthor' : myArticle.postAuthor,
                            'postPublishDate' : myArticle.postPublishDate
                        }
    dataDictionary = {'myArticleContents' : myArticleContents, 'times' : list(range(4))}
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', dataDictionary)
