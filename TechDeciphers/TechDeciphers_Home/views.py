from django.http import JsonResponse
from Notebooks.models import Notebook
from Tutorials.models import Tutorial
from django.shortcuts import render, redirect
from TechDeciphers_Home.models import DropSuggestionModel, KeepMeUpdatedEmail

def index(request):
    myNotebooks = Notebook.objects.filter(isPublished = True).order_by('-postPublishDate')[:3]
    tutorials = Tutorial.objects.filter(isPublished = True).order_by('-postPublishDate')[:3]
    homeDictionary = {'myNotebooks' : myNotebooks, 'tutorials' : tutorials}
    return render(request, 'TechDeciphers_Home/home.html', homeDictionary)

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
