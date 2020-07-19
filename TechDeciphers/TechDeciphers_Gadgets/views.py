from django.shortcuts import render
from django.core.paginator import Paginator
from TechDeciphers_Gadgets.models import Gadgets
from TechDeciphers_Gadgets.form import GadgetForm


# def index(request):
#     return render(request, 'TechDeciphers_Gadgets/index.html', {'times' : list(range(4))})

# def index(request):
#     gadgetsList = Gadgets.objects.all().order_by('-postPublishDate')
#     gadgetsDictionary = {'gadgetsList' : gadgetsList, 'times' : list(range(4))}
#     return render(request, 'TechDeciphers_Gadgets/gadgetTry.html', gadgetsDictionary)

def index(request):
    gadgetsList = Gadgets.objects.all().order_by('-postPublishDate')
    paginator = Paginator(gadgetsList, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    gadgetsDictionary = {'page_obj' : page_obj, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_Gadgets/gadgetTry.html', gadgetsDictionary)

def gadgetsForm(request):
    form = GadgetForm()

    if request.method == "POST":
        form = GadgetForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'TechDeciphers_Gadgets/gadgetsForm.html', {'form' : form})

def getArticlePostContents(request):
    articleId = request.POST.get('articlePrimaryId', None)
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
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', dataDictionary)
