from pytube import YouTube

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Downloader:
	
	# def __init__(self):
	# 	print('Welcome to YouTube Downloader appliation!')

	def downloadVideo(self):
		videoUrl = input("Enter YouTube video URL: ")
		stream = chooseVideoSteam(self, videoUrl, True)
		stream.download()
		print("{} successfully downloaded!".format(stream.default_filename))

	def downloadVideo(self, videoUrl):
		stream = self.chooseVideoSteam(videoUrl, False)
		stream.download()
		print("{} successfully downloaded!".format(stream.default_filename))

	def chooseVideoSteam(self, videoUrl, manualMode):
		if manualMode == False:
			return YouTube(videoUrl).streams.first()
		else:
			video = YouTube(videoUrl)
			print(video.title)
			streams = video.streams.all()
			i = 1
			for stream in streams:
				print(str(i) + ": " + str(stream))
				i += 1
			choice = int(input("Choose video stream: "))
			return streams[choice - 1]

	def downloadPlaylist(self, playlistUrl):
		driver = webdriver.Chrome()
		driver.get(playlistUrl)
		try:
			# global elements
			elements = WebDriverWait(driver, 3).until(
				EC.presence_of_all_elements_located((By.XPATH, "//a[@class='style-scope ytd-playlist-video-renderer']")) 
			)
			for e in elements:
				print(e.text + " - " + e.get_attribute('href'))
				self.downloadVideo(e.get_attribute('href'))
		finally:
			driver.quit()
		

dl = Downloader()
playlistUrl = input('Enter playlist URL: ')
# dl.downloadPlaylist('https://www.youtube.com/playlist?list=PLC890D2C32BFBE0A5')
dl.downloadPlaylist(playlistUrl)