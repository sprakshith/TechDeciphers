from django.shortcuts import render, redirect
from django.http import HttpResponse
from TechDeciphers_Gadgets.models import Gadgets
from TechDeciphers_News.models import News
from TechDeciphers_Leaks.models import Leaks
from TechDeciphers_TopX.models import TopX

def index(request):
        gadgetsList = Gadgets.objects.all().order_by('-postPublishDate')[:3]
        newsList = News.objects.all().order_by('-postPublishDate')[:2]
        leaksList = Leaks.objects.all().order_by('-postPublishDate')[:2]
        topXList = TopX.objects.all().order_by('-postPublishDate')[:2]
        homeDictionary = {
                            'gadgetsList' : gadgetsList,
                            'newsList' : newsList,
                            'leaksList' : leaksList,
                            'topXList' : topXList,
                            'times' : list(range(3))
                         }

        return render(request, 'TechDeciphers_Home/home.html', homeDictionary)

def getArticlePostContents(request):
    articleId = request.POST.get('articlePrimaryId', None)
    articleType = request.POST.get('articleType', None)
    dataDictionary = {}

    if articleType == "gadget":
        myArticle = Gadgets.objects.filter(gadgetId = articleId)[0]
        myArticleContents = {
                                'articleImage' : myArticle.gadgetImage,
                                'heading' : myArticle.heading,
                                'miniHeading' : myArticle.miniHeading,
                                'miniContent' : myArticle.miniContent,
                                'completeContent' : myArticle.completeContent,
                                'postAuthor' : myArticle.postAuthor,
                                'postPublishDate' : myArticle.postPublishDate
                            }
        dataDictionary = {'myArticleContents' : myArticleContents, 'times' : list(range(4))}

    elif articleType == "news":
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

    elif articleType == "topX":
        myArticle = TopX.objects.filter(topXId = articleId)[0]
        myArticleContents = {
                                'articleImage' : myArticle.topXImage,
                                'heading' : myArticle.heading,
                                'miniHeading' : myArticle.miniHeading,
                                'completeContent' : myArticle.completeContent,
                                'postAuthor' : myArticle.postAuthor,
                                'postPublishDate' : myArticle.postPublishDate
                            }
        dataDictionary = {'myArticleContents' : myArticleContents, 'times' : list(range(4))}

    elif articleType == "leaks":
        myArticle = Leaks.objects.filter(leakId = articleId)[0]
        myArticleContents = {
                                'articleImage' : myArticle.leakImage,
                                'heading' : myArticle.heading,
                                'miniHeading' : myArticle.miniHeading,
                                'completeContent' : myArticle.completeContent,
                                'postAuthor' : myArticle.postAuthor,
                                'postPublishDate' : myArticle.postPublishDate
                            }
        dataDictionary = {'myArticleContents' : myArticleContents, 'times' : list(range(4))}

    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', dataDictionary)

def getSearchedArticlePostContents(request):
    searchValue = request.POST.get('seachArticleName', None)

    gadgetsList = Gadgets.objects.filter(heading__icontains = searchValue)[:3]
    newsList = News.objects.filter(heading__icontains = searchValue)[:2]
    leaksList = Leaks.objects.filter(heading__icontains = searchValue)[:2]
    topXList = TopX.objects.filter(heading__icontains = searchValue)[:2]

    homeDictionary = {
                        'gadgetsList' : gadgetsList,
                        'newsList' : newsList,
                        'leaksList' : leaksList,
                        'topXList' : topXList,
                        'times' : list(range(3))
                     }

    return render(request, 'TechDeciphers_Home/home.html', homeDictionary)
