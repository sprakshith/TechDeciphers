from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from Notebooks.form import NotebookForm
from Notebooks.models import Notebook


def index(request):
    notebooks = Notebook.objects.filter(isPublished = True).order_by('-postPublishDate')
    paginator = Paginator(notebooks, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    notebooksDictionary = {'page_obj' : page_obj}
    return render(request, 'Notebooks/notebooks.html', notebooksDictionary)


def notebook_form(request):
    form = NotebookForm()

    if request.method == "POST":
        form = NotebookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/my_notebooks')
        else:
            print(form.errors)

    return render(request, 'Notebooks/notebook_form.html', {'form' : form})


def get_article_contents(request):
    article_id = request.GET.get('article_primary_id', None)
    my_article = Notebook.objects.filter(notebook_id = article_id)[0]
    my_article_contents = {
                            'article_image' : my_article.notebook_image,
                            'heading' : my_article.heading,
                            'description' : my_article.description,
                            'content' : my_article.content,
                            'postAuthor' : my_article.postAuthor,
                            'postPublishDate' : my_article.postPublishDate
                        }
    data_dictionary = {'my_article_contents' : my_article_contents}
    return render(request, 'CommonTemplates/ArticlePost/article_post.html', data_dictionary)
