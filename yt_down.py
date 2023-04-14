from audioDownloader import AudioDownloader
from videoDownloader import VideoDownloader 
from playlistDownloader import PlaylistDownloader
from pathlib import Path
from pytube import YouTube


operation = input('1. Video \n2. Audio\n3. Playlist\n')
link = input("Enter the YouTube video URL: ")
print("Enter the directory (leave blank for current directory)")
save_path = input(">> ")

switcher = {
    "1": lambda: VideoDownloader(link, save_path, input('Resolution: \n1.MAX\n2.MIN\n3.360p\n4.720p\n')).download(),
    "2": lambda: AudioDownloader(link, save_path).download(),
    "3": lambda: PlaylistDownloader(link, save_path).download()
}
action = switcher.get(operation, None)
if action is None:
    print("Invalid input")
    exit(1)
action()

