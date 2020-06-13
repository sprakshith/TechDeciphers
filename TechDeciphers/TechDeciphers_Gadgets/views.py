from django.shortcuts import render
from TechDeciphers_Gadgets.models import Gadgets
from TechDeciphers_Gadgets.form import GadgetForm


def index(request):
    return render(request, 'TechDeciphers_Gadgets/index.html', {'times' : list(range(4))})

def gadgetsTry(request):
    gadgetsList = Gadgets.objects.all().order_by('-postPublishDate')
    gadgetsDictionary = {'gadgetsList' : gadgetsList, 'times' : list(range(4))}
    return render(request, 'TechDeciphers_Gadgets/gadgetTry.html', gadgetsDictionary)

def gadgetsForm(request):
    form = GadgetForm()

    if request.method == "POST":
        form = GadgetForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'TechDeciphers_Gadgets/gadgetsForm.html', {'form' : form,'times' : list(range(4))})

def gadgetsArticlePost(request):
    return render(request, 'CommonTemplates/ArticlePost/articlePost.html', {'times' : list(range(4))})
