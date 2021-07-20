from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_http_methods

from .models import Media, Favourite


def audio(request):
    queryset = Media.objects.all().filter(Media_type='Audio')
    return render(request, 'audios.html' , {'audio': queryset})


def video(request):
    queryset = Media.objects.all().filter(Media_type='Video')
    return render(request, 'Videos.html' , {'video': queryset})


@require_http_methods(["GET"])
def favourite(request, user, Media_id):
    queryset = Favourite.objects.all().filter(user='%s' % user, Media_id='%s' % Media_id)
    if len(queryset) == 0:
        isfavourite=False
    elif len(queryset) == 1:
        isfavourite=True
    else:
        isfavourite="Something went wrong in isfavourite"
    popularity = Favourite.objects.all().filter(Media_id='%s' % Media_id).count()
    context = {
        'isfavourite': isfavourite,
        'popularity': popularity,
    }
    return render(request, 'favouriteGet.html', context)

@require_http_methods(["POST"])
def favouritePost(request):
    mid = request.path.split('/')[-1]
    user = request.path.split('/')[-2]
    return 'hello'
