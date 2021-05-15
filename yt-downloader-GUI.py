"""
Youtube video and audio downloader using Tkinter, Pytube, youtube_dl modules of python3.

This script can download any youtube video and audio of any youtube video in your system,by just providing the correct youtube video link.

Author : Lucky Verma (https://github.com/luckyverma-sudo)
Created on : May 11, 2021

last modified by : Lucky verma (https://guthub.com/luckyverma-sudo)
on : May 15, 2021

Changes made in last modification:
1. Changed old labels and code.
2. Added new function to download video.
3. Changed almost all old code.

Authors contributed to this script (Add your name below if you have contributed) :
1. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:@gmail.com)
"""

# Importing required modules and functions
try:
    from tkinter import *
    from tkinter import messagebox as mb
    from pytube import YouTube
    from youtube_dl import YoutubeDL

except Exception as e:
    # This will show error if the following modules are not installed on your device
    print(f"\n[ Error : {e} ]\nPress enter to continue... ")

# defining function for downloading audio only of youtube videos
def download_audio():
    URL = link.get()
    video_details = YouTube(f'{URL}')

    audio_downloader = YoutubeDL({'format': 'bestaudio'})

    while True:
        try:
            mb.showinfo(
                'Downloading', 'Downloading...')
            # Main work/Algorithm of this tool, who downloads the audio
            audio_downloader.extract_info(URL)

            # printing your video details
            mb.showinfo(
                'Audio Details', f"Title - {video_details.title}\nLength - {video_details.length} seconds\nRating - {video_details.rating}\nViews - {video_details.views} views")
            link.delete(0, END)
            mb.showinfo(
                'message', "Your audio is successfully downloaded in the same folder as our tool!")
            break
        except Exception:
            #  this will show error if the link given is broken or not completed
            mb.showerror(
                'error', "Couldn\'t download the audio,maybe due to invalid link!")
            break

# defining function for downloading youtube videos
def download_video():
    URL = link.get()
    youtube = YouTube(f'{URL}')
    link.delete(0, END)
    while True:
        try:
            mb.showinfo('Downloading', "Downloading...")
            # mb.showinfo('message', "please wait...")
            video = youtube.streams.first()
            video.download()
            mb.showinfo(
                'Audio Details', f"Title - {youtube.title}\nLength - {youtube.length} seconds\nRating - {youtube.rating}\nViews - {youtube.views} views")
            mb.showinfo(
                'message', "Your video is successfully downloaded in the same folder as our tool!")
            break

        except Exception:
            mb.showerror(
                'error', "Error,Couldn\'t download the audio,maybe due to invalid link!")
            break

# fumction to terminate the preogramme/Application
def exit_tool():
    mb.showwarning('Terminating', "Click 'Ok' to terminate our Application!")
    root.destroy()


root = Tk()

root.title("Youtube downloader by lucky verma")
root.config(background="black")
root.geometry("550x350")
root.minsize(550, 350)
root.maxsize(550, 350)

title = Label(root, text="Youtube Downloader", background="black",
              foreground="cyan", font=("serif 28")).place(x=100, y=50)

label = Label(root, text="Paste the video link below :", background="black",
              foreground="cyan", font=("consolas 14")).place(x=110, y=130)

link = Entry(root, width=40, background="black", foreground="cyan",
             font=("consolas 14"))
link.place(x=50, y=170)

audio = Button(root, text="Download audio", background="black",
               foreground="cyan", font=(15), command=download_audio).place(x=50, y=240)

video = Button(root, text="Download video", background="black",
               foreground="cyan", font=(15), command=download_video).place(x=340, y=240)

exit = Button(root, text="EXIT", background="black",
              foreground="cyan", font=(15), command=exit_tool).place(x=243, y=285)

# starting our programme
root.mainloop()