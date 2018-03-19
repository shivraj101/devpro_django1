# from django.http import HttpResponse
# from .models import Album, Song
# # from django.template import loader
# from django.shortcuts import render, get_object_or_404
# # from django.http import Http404
#
#
# #/music/
# def index(request):
#     all_albums = Album.objects.all()
#     context = {
#         'all_albums': all_albums,
#     }
#     return render(request, 'music/index.html', context)
# #/music/first
# def first_page(request):
#     return HttpResponse("<h2>This is my own first data!!</h2>")
#
# #/music/71
# def detail(request,album_id):
#     # return HttpResponse("<h2>Details for Album id:"+str(album_id)+"</h2>")
#
#     # try:
#     #     album = Album.objects.get(id=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist!!")
#     album = get_object_or_404(Album, pk = album_id)
#     return render(request, 'music/detail.html', {'album':album})
#
# #/music/<album.id>/favourite
# def favourite(request,album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message':'You did not select a valid song!!!!!'
#         })
#     else:
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})
#
#
from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')