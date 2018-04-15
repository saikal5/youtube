import youtube_dl
from .forms import LinkForm
from .models import Link
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect

def download_video(request):

    form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'input.html', context)

def download_video1(request):
    form = LinkForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            youtubeUrl = request.POST.get('url') # Получаем ссылку с формы

            url = Link(url=youtubeUrl) # Сохроняем запись в БД
            url.save()

            options = { # Настройки youtube_dl
                'outtmpl': '%(title)s-%(id)s.%(ext)s',
                'format': 'best'
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                r = ydl.extract_info(youtubeUrl, download=False) # Вставляем нашу ссылку с ютуба
                videoUrl = r['webpage_url'] # Получаем прямую ссылку на скачивание видео
                print(videoUrl)

            name = 'test'
            response = HttpResponsePermanentRedirect(videoUrl) # Вставляем прямую ссылку на скачивание в редирект
            response['content_type'] = 'application/force-download'
            response['Content-Disposition'] = 'attachment; filename=%s' % name

            return response
        else:
            print('Form is not valid!')

