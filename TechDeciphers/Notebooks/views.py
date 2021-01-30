from django.shortcuts import render
from Notebooks.models import Notebook
from django.core.paginator import Paginator


def index(request):
    return HttpResponse('Hello from the Notebook Page')
