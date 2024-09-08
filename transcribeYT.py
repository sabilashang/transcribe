import whisper
from pytube import YouTube
import static_ffmpeg

static_ffmpeg.add_paths()
youtube_links = ["https://www.youtube.com/", "https://youtu.be/", "https://y2u.be/"]

def getStream(link):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(filename="audio.mp3")
    print("Stream Identified...")
    print("-------------------------------------------------")    

def transcript(title):
    model = whisper.load_model("base")
    script = model.transcribe("audio.mp3", fp16=False,)
    print("Transcription Complete...")
    content = script["text"]
    print("-------------------------------------------------")
    
    with open(title, 'w', encoding='utf-8') as file:
        file.write(content)        

    print(f"Transcription saved to {title}...")
    print("-------------------------------------------------")

print("Enter the URL: ", end="")
url = str(input())

if any(link in url for link in youtube_links):
    print("Processing...")
    getStream(url)

    print("Save as: ", end="")
    name = str(input()) + ".doc"
    transcript(name)

else:
    print("Please make sure the link provided is suitable...")
    print("The Allowed Formats: ")
    for link in youtube_links:
        print(f"        {link}")
    print("-------------------------------------------------")
