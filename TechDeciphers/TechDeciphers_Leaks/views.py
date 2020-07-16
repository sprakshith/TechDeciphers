from django.shortcuts import render
from TechDeciphers_Leaks.models import Leaks
from TechDeciphers_Leaks.form import LeaksForm

# def index(request):
#     return render(request, 'TechDeciphers_Leaks/leaks.html', {'times' : list(range(4))})

def index(request):
    leaksList = Leaks.objects.all().order_by('-postPublishDate')
    leaksDictionary = {'leaksList' : leaksList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_Leaks/leaksView.html', leaksDictionary)

def leaksForm(request):
    form = LeaksForm()

    if request.method == "POST":
        form = LeaksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'TechDeciphers_Leaks/leaksForm.html', {'form' : form})

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
