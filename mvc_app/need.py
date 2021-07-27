from .models import Media, Favourite


def fav(request, Media_id):
    """function  for get liked or not"""
    user = request.user
    return Favourite.objects.all().filter(user=user, Media_id=Media_id)


def pop(request, Media_id):
    """Function for get popularity"""
    popularity = Favourite.objects.all().filter(Media_id=Media_id).count()
    return popularity

#queryset = Media.objects.all().filter(Media_type='Audio'). \
        #annotate(like=fav(request, F("Media_id")))
