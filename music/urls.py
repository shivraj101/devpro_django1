from django.conf.urls import url
from . import views

app_name = 'music' #namespace

urlpatterns = [
    #/music/
    # url(r'^$',views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/first ......to test another url connection
    # url(r'^first$', views.first_page, name='first'),#first_page is a function

    #/music/71(album_id but in the beginning I used as a random id)
    # url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/71/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite$',views.favourite,name='favourite'),

    #/music/album/add
    url(r'^album/add/$',views.AlbumCreate.as_view(), name='add-album'),

    #/music/album/71
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='update-album'),

    #/music/album/71/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='delete-album'),
]
