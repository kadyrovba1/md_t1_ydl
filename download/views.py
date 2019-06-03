from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DownloadForm
from .models import Download
import youtube_dl


def index(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        Download.objects.create(upload=url)
        options = {'format': 'best'}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
    return render(request, 'download/index.html', {'form': form})