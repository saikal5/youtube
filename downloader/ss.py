import youtube_dl

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
v_formats = video
print(video)

