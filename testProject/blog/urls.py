from django.urls import path
from . import views
from django.conf.urls import url

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    #path('post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]