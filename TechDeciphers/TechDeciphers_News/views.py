from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from TechDeciphers_News.models import News
from TechDeciphers_News.form import NewsForm
from django.http import JsonResponse

# def index(request):
#     return render(request, 'TechDeciphers_News/news.html', {'times' : list(range(4))})

# def index(request):
#     newsList = News.objects.all().order_by('-postPublishDate')
#     newsDictionary = {'newsList' : newsList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_News/newsView.html', newsDictionary)

def index(request):
    newsList = News.objects.filter(isPublished = True).order_by('-postPublishDate')
    paginator = Paginator(newsList, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    newsDictionary = {'page_obj' : page_obj, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_News/newsView.html', newsDictionary)


@login_required(login_url="/errorPageNotFound/")
def newsForm(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/news')
        else:
            print(form.errors)

    return render(request, 'TechDeciphers_News/newsForm.html', {'form' : form})

# def tryingAjaxCall(request):
#     print("Came Inside Without Anyproblem, Thanks to Ajax")
#     currentArticleId = request.GET.get('primary_key', None)
#     return JsonResponse({})

def getArticlePostContents(request):
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
