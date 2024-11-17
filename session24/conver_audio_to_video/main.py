from time import time
from moviepy import editor

urls = [
    'conver_audio_to_video/videos/IMG_1501.MP4',
    'conver_audio_to_video/videos/IMG_2260.MOV',
    'conver_audio_to_video/videos/IMG_2535.MOV',
    'conver_audio_to_video/videos/IMG_3303.MP4',
    'conver_audio_to_video/videos/IMG_3308.MP4'
]


def convert(url):
    name = url.rsplit('.', 1)[0] + '.mp3'
    
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(name)
    print(f"Converted {url} to {name}")

start_time = time()

for url in urls:
    convert(url)

end_time=time()

print(end_time-start_time)