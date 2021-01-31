from django.shortcuts import render
from Notebooks.models import Notebook
from django.core.paginator import Paginator


def index(request):
    notebooks = Notebook.objects.filter(isPublished = True).order_by('-postPublishDate')
    paginator = Paginator(notebooks, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    notebooksDictionary = {'page_obj' : page_obj}
    return render(request, 'Notebooks/notebooks.html', notebooksDictionary)
