from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Media, Favourite


def index(request):
    return render(request, 'hello.html')


def audio(request):
    all_audio = Media.objects.all().filter(Media_type='audio')
    #return render(request, 'hello.html', all_audio)
    template =loader.get_template('hello.html')
    context = {
        'audio': all_audio,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
