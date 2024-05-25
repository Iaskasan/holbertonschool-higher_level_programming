from pytube import YouTube

def download_video(URL="", Path=""):
    
    URL = input("URL of the video: ")
    Path = input("Choose the path for the downloaded video: ")
    yt = YouTube(URL)
    stream = yt.streams.get_highest_resolution()
    print("Downloading...")
    stream.download(output_path=Path)
    print("Dowload complete!")

def download_audio(URL="", Path=""):
    URL = input("URL of the video: ")
    Path = input("Choose the path for the downloaded video: ")
    yt = YouTube(URL)
    audio_stream = yt.streams.filter(only_audio=True).first()
    print("Downloading...")
    audio_stream.download(output_path=Path)
    print("Dowload complete!")

download_audio()