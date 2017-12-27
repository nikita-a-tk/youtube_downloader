from pytube import YouTube
print("Welcome to YouTube Downloader app!")
video_url = input("Which video you want to download?\n")
# video_url = "https://www.youtube.com/watch?v=M0Ypzm7pVw4" # short video for testing
video = YouTube(video_url)
print(video.title)
streams = video.streams.all()
i = 1
for stream in streams:
	print(str(i) + ": " + str(stream))
	i += 1

choice = int(input("Choose video stream: "))

streams[choice - 1].download()

print("{} successfully downloaded!".format(streams[choice - 1].default_filename))