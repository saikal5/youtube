from django.urls import path
from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('', views.download_video, name='download_video'),
]
