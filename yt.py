from pytube import YouTube as yt
import os

path = "/storage/emulated/0/YT Downloader"

def yt_video():
		yt_vid = yt(url).streams.get_highest_resolution()
		print("Downloading......")
		yt_vid.download(output_path=path)
		print("Download Video Sucessfully\nPath:",path)
	
def yt_audio():
		yt_aud = yt(url).streams.filter(only_audio=True).first()
		print("Downloading.....")
		dwn = yt_aud.download(output_path=path)
		base, ext = os.path.splitext(dwn)
		new_name = base + '.mp3'
		os.rename(dwn, new_name)
		print("Download Audio Sucessfully\nPath:",path)
		
while True:
	os.system("clear")
	print("YouTube Downloader By:\n  Author : K卂丂工乇从\n  Thanks To : All\nThanks To ause This Script, See You\nPath:",path)
	url = input("Link: ")
	print("\nTitle:",yt(url).title,"\n\nDownload Video Or Audio\n  1.Video\n  2.Audio\nNote: Only Downlad for Youtube")
	usr_input = input("Choose: ")
	if usr_input == "1":
		yt_video()
	elif usr_input == "2":
		yt_audio()
	else:
		print("Thank You")
		exit()
