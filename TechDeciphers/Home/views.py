from django.http import JsonResponse
from Notebooks.models import Notebook
from Tutorials.models import Tutorial
from django.shortcuts import render, redirect
from Home.models import DropSuggestionModel, KeepMeUpdatedEmail


def index(request):
    myNotebooks = Notebook.objects.filter(isPublished = True).order_by('-postPublishDate')[:3]
    tutorials = Tutorial.objects.filter(isPublished = True).order_by('-postPublishDate')[:3]
    homeDictionary = {'myNotebooks' : myNotebooks, 'tutorials' : tutorials}
    return render(request, 'Home/home.html', homeDictionary)


def get_article_contents(request):
    article_id = request.GET.get('article_primary_id', None)
    article_type = request.GET.get('article_type', None)
    data_dictionary = {}

    if article_type == "NOTEBOOK":
        myArticle = Notebook.objects.filter(notebook_id = article_id)[0]
        my_article_contents = {
                                'article_image' : myArticle.notebook_image,
                                'heading' : myArticle.heading,
                                'description' : myArticle.description,
                                'content' : myArticle.content,
                                'postAuthor' : myArticle.postAuthor,
                                'postPublishDate' : myArticle.postPublishDate
                            }
        data_dictionary = {'my_article_contents' : my_article_contents}
    elif article_type == "TUTORIAL":
        myArticle = Tutorial.objects.filter(tutorial_id = article_id)[0]
        my_article_contents = {
                                'article_image' : myArticle.tutorial_image,
                                'heading' : myArticle.heading,
                                'description' : myArticle.description,
                                'content' : myArticle.content,
                                'postAuthor' : myArticle.postAuthor,
                                'postPublishDate' : myArticle.postPublishDate
                            }
        data_dictionary = {'my_article_contents' : my_article_contents}

    return render(request, 'CommonTemplates/ArticlePost/article_post.html', data_dictionary)


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