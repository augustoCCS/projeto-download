from pytube import YouTube
from pathlib import Path
from os import startfile
from pywebio.input import input
from pywebio.output import put_text

def video_download():
    while True:
        video_link = input("Informe o link do vídeo: ")
        if video_link.startswith("https:"):
            try:
                put_text("Fazendo download do vídeo...".title()).style('color: red; font-size: 50px')
                video_url = YouTube(video_link)
                video_stream = video_url.streams.get_highest_resolution()
                path_to_download = Path(r"C:\Users\pc\Desktop")
                video_stream.download(output_path=path_to_download)
                put_text("Vídeo baixado com sucesso...".title()).style('color: blue; font-size: 50px')
                startfile(path_to_download / (video_url.title() + ".mp4"))
            except Exception as e:
                put_text(f"Erro ao baixar o vídeo: {e}").style('color: red; font-size: 50px')

if __name__ == "__main__":
    video_download()
