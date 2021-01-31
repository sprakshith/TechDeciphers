from django.shortcuts import render
from Tutorials.models import Tutorial
from django.core.paginator import Paginator

def index(request):
    tutorials = Tutorial.objects.filter(isPublished = True).order_by('-postPublishDate')
    paginator = Paginator(tutorials, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tutorialsDictionary = {'page_obj' : page_obj}
    return render(request, 'Tutorials/tutorials.html', tutorialsDictionary)
