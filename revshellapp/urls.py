from django.urls import path
from revshellapp import views

urlpatterns = [
    path('', views.index),
    path('enter', views.enter, name='enter'),
    path('response', views.response, name='response'),
    path('enterres', views.enterres, name="enter response"),
    path('showcmds', views.showcmds, name="show commands"),
]
