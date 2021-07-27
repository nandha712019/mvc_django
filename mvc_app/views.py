from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F, Exists, Case, When, Value, IntegerField, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Media, Favourite
from .need import fav, pop


def sign_up(request):
    """ sign up view"""
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response = redirect('/accounts/login/')
            return response
        if not form.is_valid():
            context['details'] = 'Details something wrong in the form. Please Enter again'
    context['form']=form
    return render(request,'registration/sign_up.html',context)



@login_required
def audio(request):
    """ audio view for audio details"""
    queryset = Media.objects.all().filter(Media_type='Audio').\
        annotate(like=Exists(fav(request, F('Media_id'))), popularity=Value(pop(request, F('Media_id'))))
    return render(request, 'audios.html' , {'audio': queryset})


@login_required
def video(request):
    """video view for video details"""
    context = {}
    isfavourite = []
    popularity = []
    queryset = Media.objects.all().filter(Media_type='Video')
    for m in queryset.iterator():
        d = m.Media_id
        isfavourite.append(fav(request, d))
        popularity.append(pop(request, d))
    context['isfavourite'] = isfavourite
    context['popularity'] = popularity
    return render(request, 'videos.html' , {'video': queryset, 'details': context})


def favourite_get(request, Media_id):
    """endpoint for get liked or not"""
    user = request.user
    queryset = Favourite.objects.all().filter(user=user, Media_id=Media_id)
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
    return render(request, 'favourite_get.html', context)


def favourite_post(request, Media_id):
    """endpoint for post like"""
    user = request.user
    media = Media.objects.get(Media_id=Media_id)
    f = Favourite(user=user, Media_id=media)
    if len(Favourite.objects.all().filter(user=user, Media_id=media)) >= 1:
        return HttpResponse("That like is already exists", status=400)
    f.save()
    return HttpResponse('created Successfully', status=200)


def favourite_delete(request, Media_id):
    """endpoint for delete favourite"""
    user = request.user
    if user and Media_id is None:
        return HttpResponse("bad request", status=400)
    Favourite.objects.filter(user=user, Media_id=Media_id).delete()
    return HttpResponse("Deleted Successfully", status=200)
