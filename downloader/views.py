import youtube_dl
from .forms import LinkForm
from .models import Link
from django.shortcuts import render, redirect

def download_video(request):

    form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'input.html', context)

def video(request):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            'https://www.youtube.com/watch?v=k_QW_jmCLG0',
            download=False
        )

    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    v_formats = video['formats']
    v_urls = [ x['url'] for x in v_formats if x['ext'] == 'mp4' and (x['height'] == 360 or x['height'] == 480) ]
    v_url = v_urls[0]
    return redirect(v_url)


