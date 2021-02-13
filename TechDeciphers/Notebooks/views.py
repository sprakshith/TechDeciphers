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
