from django.http import HttpResponse
from .models import Album,Song
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
def index(request):
	albums  = Album.objects.all()
	songs = Song.objects.all()
	query=request.GET.get('q')
	if query:
		albums = albums.filter(
			Q(album_title__icontains=query) |
			Q(artist__icontains=query)
		).distinct()
		songs = songs.filter(
			Q(song_title__icontains=query)
		).distinct()
		return render(request, 'music/index.html', {
           	'albums': albums,
           	'songs' : songs,
        })
	else:
		return render(request, 'music/index.html', {'albums':albums})
	
def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html',{'album':album})
