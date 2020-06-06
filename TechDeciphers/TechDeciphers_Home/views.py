from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Inside the TechDeciphers Home Page, Templates are yet to be Created. Copy and Paste any of the below Links. ' +
                         'Append any one of these links to the URL : /gadgets , /news , /topX , /leaks')
