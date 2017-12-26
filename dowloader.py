from pytube import YouTube
print("Welcome to YouTube Downloader app!")
#video_url = input("Which video you want to download?\n")
video_url = "https://www.youtube.com/watch?v=M0Ypzm7pVw4"
videos = YouTube(video_url).streams.all()

for v in videos:
	print(v)
