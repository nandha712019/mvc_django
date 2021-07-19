from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Media, Favourite


def audio(request):
    queryset = Media.objects.all().filter(Media_type='Audio')
    return render(request, 'audios.html' , {'audio': queryset})


def video(request):
    queryset = Media.objects.all().filter(Media_type='Video')
    return render(request, 'Videos.html' , {'video': queryset})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
