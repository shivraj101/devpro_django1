from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.shortcuts import render
from django.http import Http404


#/music/
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)
#/music/first
def first_page(request):
    return HttpResponse("<h2>This is my own first data!!</h2>")

#/music/71
def detail(request,album_id):
    # return HttpResponse("<h2>Details for Album id:"+str(album_id)+"</h2>")

    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist!!")
    return render(request, 'music/detail.html', {'album':album})



