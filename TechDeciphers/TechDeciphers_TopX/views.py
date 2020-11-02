from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from TechDeciphers_TopX.models import TopX
from TechDeciphers_TopX.form import TopXForm

# def index(request):
#     return render(request, "TechDeciphers_TopX/topX.html", {'times' : list(range(4)), 'times2' : list(range(8))})

# def index(request):
#     topXList = TopX.objects.all().order_by('-postPublishDate')
#     topXDictionary = {'topXList' : topXList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_TopX/topXView.html', topXDictionary)

def index(request):
    topXList = TopX.objects.filter(isPublished = True).order_by('-postPublishDate')
    paginator = Paginator(topXList, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    topXDictionary = {'page_obj' : page_obj, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_TopX/topXView.html', topXDictionary)


@login_required(login_url="/errorPageNotFound/")
def trendingForm(request):
    form = TopXForm()

    if request.method == "POST":
        form = TopXForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/topX')
        else:
            print(form.errors)

    return render(request, 'TechDeciphers_TopX/topXForm.html', {'form' : form})

def getArticlePostContents(request):
    articleId = request.GET.get('articlePrimaryId', None)
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
