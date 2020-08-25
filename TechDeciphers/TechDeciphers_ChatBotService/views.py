from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from TechDeciphers_Gadgets.models import Gadgets
from TechDeciphers_News.models import News
from TechDeciphers_Leaks.models import Leaks
from TechDeciphers_TopX.models import TopX

def getCurrentCommands():
    commands = '''
                  Below are the Commands, you can use Numbers or Type the Command Itself\n
                  1. ShowUnpublishedArticle - This Shows all the Unpublished Articles\n
                  2. WeeksArticleTarget - This Shows the remaining amounts of Articles to be uploaded this week
               '''

    return commands

@csrf_exempt
def index(request):
    receivedString = request.POST.get('Body', 'NA')
    r = MessagingResponse()

    if receivedString == 'Help' or receivedString == '0':
        r.message(getCurrentCommands())
    elif receivedString == 'ShowUnpublishedArticle' or receivedString == '1':
        r.message("There are No Unpublished Articles right Now")
    elif receivedString == 'WeeksArticleTarget' or receivedString == '2':
        r.message("Gagan : 1 Remaining\n Rakshith : 2 Remaining")
    else:
        r.message("Sorry, your Command is Not Recognised. Send 'Help' to get all the commands. Thank You.")

    return HttpResponse(r, content_type='text/xml')
