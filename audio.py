import os

def extract_audio(video_path, output_audio):
    command = f'ffmpeg -i "{video_path}" -q:a 0 -map a "{output_audio}" -y'
    os.system(command)