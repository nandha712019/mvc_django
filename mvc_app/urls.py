from django.urls import path

from . import views

urlpatterns = [
    path('audio/', views.audio, name='audio'),
    path('video/', views.video, name='video'),
    path('favourite/<str:user>/<str:Media_id>/', views.favourite, name='getFavourite'),
]
