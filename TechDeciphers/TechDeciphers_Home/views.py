from django.http import JsonResponse
from django.shortcuts import render, redirect
from TechDeciphers_Home.models import DropSuggestionModel, KeepMeUpdatedEmail

def index(request):
    homeDictionary = {}
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

def error404PageNotFound(request):
    return render(request, 'CommonTemplates/Error_Pages/loginRequired.html', {})

def aboutUsPage(request):
    return render(request, 'CommonTemplates/AboutUs/aboutUs.html', {})
