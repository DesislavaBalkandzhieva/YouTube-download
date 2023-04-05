from pytube import YouTube

def download_video(link, save_path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(save_path) 
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
save_path = r"C:/Users/Desi_Balk/PycharmProjects/YouTube downloader" # using forward slashes or double backslashes
download_video(link, save_path)
