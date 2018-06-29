
# Create your views here.
from django.http import HttpResponse,JsonResponse, Http404, request, response
import feedparser
from django.template import loader
from django.shortcuts import render, loader
from .models import Message_forum
import datetime
from django.views.decorators.csrf import csrf_protect

# Create your views here.



def welcome(request):
    msg_data = Message_forum.objects.all()
    context = {
        'msg_data': msg_data,
        'last_visit': datetime.datetime.now(),
    }
    return render(request, 'forum/welcomePage.html', context)

@csrf_protect
def post_message(request):
    msg_content = request.GET.get('msg_content')
    msg_author = request.GET.get('msg_author')
    msg_title = request.GET.get('msg_title')
    list_of_messages = Message_forum(title=msg_title, content=msg_content, author=msg_author)
    list_of_messages.save()
    msg_data = Message_forum.objects.all()
    context = {
        'msg_data': msg_data,
        'last_visit': datetime.datetime.now(),
    }
    return render(request, 'forum/welcomePage.html', context)