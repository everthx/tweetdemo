from django.conf.urls import url
from . import views
#hola

urlpatterns =[ 
    url(r'^$', views.home),
    url('about/', views.about),
    url('index/', views.index),
    
    ]