from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from Tutorials.form import TutorialForm
from Tutorials.models import Tutorial


def index(request):
    tutorials = Tutorial.objects.filter(isPublished = True).order_by('-postPublishDate')
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

    return render(request, 'Tutorials/tutorial_form.html', {'form' : form})
