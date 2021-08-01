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
    further_read_article_dict = get_further_read_article(article_id)
    my_article_contents = {
                            'article_image' : my_article.notebook_image,
                            'heading' : my_article.heading,
                            'description' : my_article.description,
                            'content' : my_article.content,
                            'postAuthor' : my_article.postAuthor,
                            'postPublishDate' : my_article.postPublishDate
                          }
    if further_read_article_dict:
        my_article_contents.update(further_read_article_dict)

    data_dictionary = {'my_article_contents' : my_article_contents}
    return render(request, 'CommonTemplates/ArticlePost/article_post.html', data_dictionary)

def get_further_read_article(article_id):
    further_read_article_dict = None
    try:
        article_id = int(article_id)
        notebooks = Notebook.objects.filter(isPublished = True)
        notebooks_ids = []
        for notebook in notebooks:
            notebooks_ids.append(notebook.notebook_id)
        notebooks_ids.remove(article_id)

        further_read_article_id = notebooks_ids[min(range(len(notebooks_ids)), key = lambda i: abs(notebooks_ids[i]-article_id))]
        further_read_article = Notebook.objects.filter(notebook_id = further_read_article_id)[0]

        notebook_dict = {
            'further_read_article_id': further_read_article.notebook_id,
            'further_read_article_title': further_read_article.heading
        }

    except:
        pass

    return notebook_dict
