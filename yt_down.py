from audioDownloader import AudioDownloader
from videoDownloader import VideoDownloader 
from playlistDownloader import PlaylistDownloader
from pathlib import Path
from pytube import YouTube


operation = input('1. Video \n2. Audio\n3. Playlist\n')
link = input("Enter the YouTube video URL: ")
print("Enter the directory (leave blank for current directory)")
save_path = input(">> ")
if operation == "1":
    res=input('Resolution: \n1.MAX\n2.MIN\n3.360p\n4.720p\n')
    downloader = VideoDownloader(link, save_path, res)
elif operation == "2":
    downloader = AudioDownloader(link, save_path)
elif operation=="3":
    downloader= PlaylistDownloader(link, save_path)
else:
    print("Invalid input")
    exit(1)

downloader.download()
