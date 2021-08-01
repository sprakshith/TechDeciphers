from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from Tutorials.form import TutorialForm
from Tutorials.models import Tutorial


def index(request):
    article_id = request.GET.get('article_id', None)
    if article_id:
        tutorials = Tutorial.objects.filter(isPublished = True) \
                                    .filter(parentId = article_id) \
                                    .order_by('postPublishDate')
        tutorialsDictionary = {'page_obj' : tutorials}
        return render(request, 'Tutorials/tutorials.html', tutorialsDictionary)
    else:
        tutorials = Tutorial.objects.filter(isPublished = True) \
                                    .filter(parentId = 0) \
                                    .order_by('postPublishDate')
        paginator = Paginator(tutorials, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tutorialsDictionary = {'page_obj' : page_obj}
        return render(request, 'Tutorials/tutorials.html', tutorialsDictionary)


def tutorial_form(request):
    form = TutorialForm()

    if request.method == "POST":
        form = TutorialForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/tutorials')
        else:
            print(form.errors)

    parent_tutorials = get_parent_tutorials()
    child_tutorials = get_child_tutorials()

    context_dictionary = {
                            'form' : form,
                            'parent_tutorials' : parent_tutorials,
                            'child_tutorials' : child_tutorials
                         }

    return render(request, 'Tutorials/tutorial_form.html', context_dictionary)


def get_article_contents(request):
    article_id = request.GET.get('article_primary_id', None)
    my_article = Tutorial.objects.filter(tutorial_id = article_id)[0]
    if my_article.parentId > 0:
        my_article_contents = {
                                'article_image' : my_article.tutorial_image,
                                'heading' : my_article.heading,
                                'description' : my_article.description,
                                'content' : my_article.content,
                                'postAuthor' : my_article.postAuthor,
                                'postPublishDate' : my_article.postPublishDate
                              }

        previous_article_dict = get_adjacent_article(my_article.previousTutorial, 'previous')
        next_article_dict = get_adjacent_article(my_article.nextTutorial, 'next')

        if previous_article_dict:
            my_article_contents.update(previous_article_dict)
        if next_article_dict:
            my_article_contents.update(next_article_dict)

        data_dictionary = {'my_article_contents' : my_article_contents}
        return render(request, 'CommonTemplates/ArticlePost/article_post.html', data_dictionary)
    else:
        return HttpResponseRedirect("/tutorials?article_id=" + article_id)

def get_child_tutorials():
    tutorials = Tutorial.objects.filter(isChildPage = True).order_by('heading')
    return tutorials

def get_parent_tutorials():
    tutorials = Tutorial.objects.filter(isChildPage = False).order_by('heading')
    return tutorials

def get_adjacent_article(article_id, type):
    article_dictionary = None
    if article_id > 0:
        article = Tutorial.objects.filter(tutorial_id = article_id)[0]
        if article:
            if type == 'previous':
                article_dictionary = {
                    'previous_article_id' : article.tutorial_id,
                    'previous_article_title' : article.heading
                }
            else:
                article_dictionary = {
                    'next_article_id' : article.tutorial_id,
                    'next_article_title' : article.heading
                }

    return article_dictionary
