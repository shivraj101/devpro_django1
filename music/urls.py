from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$',views.index, name='index'),

    #/music/first ......to test another url connection
    url(r'^first$', views.first_page, name='first'),#first_page is a function

    #/music/71(random id no link to actual Album model)
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
]
