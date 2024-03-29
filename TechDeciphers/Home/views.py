from django.http import JsonResponse
from Notebooks.models import Notebook
from Tutorials.models import Tutorial
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from Home.models import DropSuggestionModel, KeepMeUpdatedEmail


def index(request):
    myNotebooks = Notebook.objects.filter(isPublished = True).order_by('-postPublishDate')[:3]
    tutorials = Tutorial.objects.filter(isPublished = True)\
                                .filter(parentId = 0)\
                                .order_by('postPublishDate')[:3]
    homeDictionary = {'myNotebooks' : myNotebooks, 'tutorials' : tutorials}
    return render(request, 'Home/home.html', homeDictionary)

def get_searched_article_content(request):
    searched_value = request.GET.get('search_article_name', None)
    tutorials = Tutorial.objects.filter(heading__icontains = searched_value, isPublished = True)
    paginator = Paginator(tutorials, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tutorialsDictionary = {'page_obj' : page_obj}

    return render(request, 'Tutorials/tutorials.html', tutorialsDictionary)


def get_tutorials_heading(request):
    searched_value = request.GET.get('q', 'pan')
    tutorials = Tutorial.objects.filter(heading__icontains = searched_value, isPublished = True)
    result_list = [tutorial.heading for tutorial in tutorials]
    return JsonResponse(result_list, safe=False)


def dropSuggestion(request):
    emailId = request.GET.get('EMAILID', None)
    suggestion = request.GET.get('SUGGESTION', None)

    if emailId != None and suggestion != None:
        modelInstance = DropSuggestionModel(suggestorEmailId = emailId, suggestiontText = suggestion)
        modelInstance.save()

    return JsonResponse({'Message' : 'Object Created Succesfully'})


def keepMeUpdated(request):
    emailId = request.GET.get('EMAILID', None)

    if emailId != None:
        modelInstance = KeepMeUpdatedEmail(newsletterEmailId = emailId)
        modelInstance.save()

    return JsonResponse({'Message' : 'Object Created Succesfully'})


def aboutUsPage(request):
    return render(request, 'CommonTemplates/AboutUs/aboutUs.html', {})
