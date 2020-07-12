from django.shortcuts import render
from TechDeciphers_Leaks.models import Leaks

# def index(request):
#     return render(request, 'TechDeciphers_Leaks/leaks.html', {'times' : list(range(4))})

def index(request):
    leaksList = Leaks.objects.all().order_by('-postPublishDate')
    leaksDictionary = {'leaksList' : leaksList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_Leaks/leaksView.html', leaksDictionary)

def getArticlePostContents(request):
    articleId = request.POST.get('articlePrimaryId', None)
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
