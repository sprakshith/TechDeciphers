from django.shortcuts import render
from TechDeciphers_TopX.models import TopX

# def index(request):
#     return render(request, "TechDeciphers_TopX/topX.html", {'times' : list(range(4)), 'times2' : list(range(8))})

def index(request):
    topXList = TopX.objects.all().order_by('-postPublishDate')
    topXDictionary = {'topXList' : topXList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_TopX/topXView.html', topXDictionary)

def getArticlePostContents(request):
    articleId = request.POST.get('articlePrimaryId', None)
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
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', dataDictionary)
