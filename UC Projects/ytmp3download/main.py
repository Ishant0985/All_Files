from pytube import YouTube 

print("Creating YouTube object...")
link = YouTube("https://www.youtube.com/watch?v=QCIAGwQnJ4Y&list=PLKPf-MHoBx0APPS4kdCi6JAaxEJwZPFuJ&index=2")
print("Selecting audio stream...")
audio_stream = link.streams.filter(only_audio=True).first()

if audio_stream is not None:
    print("Audio stream found. Downloading...")
    audio_stream.download("C:\\Users\\scien\\Downloads")
    print("Download started at C:\\Users\\scien\\Downloads")
else:
    print("No audio stream found.")
