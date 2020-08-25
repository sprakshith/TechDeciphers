from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from TechDeciphers_Gadgets.models import Gadgets
from TechDeciphers_News.models import News
from TechDeciphers_Leaks.models import Leaks
from TechDeciphers_TopX.models import TopX

from TechDeciphers_ChatBotService.ChatBotUtil.topNewGadgets import getTopNewsGadget

@csrf_exempt
def index(request):
    receivedString = request.POST.get('Body', 'NA')
    r = MessagingResponse()
    print(getTopNewsGadget(""))

    if receivedString == '/showTodaysNews':
        r.message(getTopNewsGadget(""))
    else:
        r.message("Sorry, your Command is Not Recognised")

    return HttpResponse(r, content_type='text/xml')
