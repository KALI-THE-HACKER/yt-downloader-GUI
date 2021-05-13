"""
Youtube video to audio downloader using Tkinter, Pytube, youtube_dl and Python3

This script will download audio of any youtube video in your system,by just providing the correct youtube video link.

Author : Lucky Verma (https://github.com/luckyverma-sudo)
Created on : May 11, 2021


Authors contributed to this script (Add your name below if you have contributed) :
1. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:@gmail.com)
"""

#  Importing required modules and functions
try:
    from tkinter import *
    from tkinter import messagebox as mb
    from youtube_dl import YoutubeDL
    from pytube import YouTube
    import time

except Exception as e:
    # This will show error if the following modules are not installed on your device
    print(f"\n[ Error : {e} ]\nPress enter to continue... ")


def download():
    URL = e1.get()
    video_details = YouTube(f'{URL}')
    
    audio_downloader = YoutubeDL({'format': 'bestaudio'})

    while True:
        try:
            # Main work/Algorithm of this tool, who downloads the audio
            audio_downloader.extract_info(URL)
            mb.showinfo(
                'message', f'Your audio is downloading and will be available in the same directory as our App!')
            
            # printing your video details 
            mb.showinfo(
                'Audio Details', f"Title - {video_details.title}\nLength - {video_details.length} seconds\nRating - {video_details.rating}\nViews - {video_details.views} views")
            e1.delete(0, END)
            break
        except Exception:
            #  this will show error if the link given is broken or not completed
            mb.showerror('error', "Couldn\'t download the audio,perhaps it's a broken link!")
            break

# fumction to terminate the preogramme/Application
def exit_tool():
    mb.showwarning('Terminating', "Click 'Ok' to terminate our Application!")
    time.sleep(2)
    exit()


root = Tk()

root.title("YTMP3 Downloader - by lucky verma")

root.geometry("500x300")
root.minsize(450, 270)
root.maxsize(500, 300)
root.config(background = "black")

bg = "black"
fg = "cyan"

blank_label = Label(root, text="", bg = bg).pack()

main_label = Label(root, text="YTMP3 Downloader", font=(
    "consolas", 24, "bold"), borderwidth=5,
    bg=bg, fg=fg)
main_label.pack()

frame = Frame(root).pack()
blank_label = Label(root, text="", bg = bg, fg = fg).pack()
l1 = Label(frame, text="Enter Youtube video URL below:",
           font=(18), bg = bg, fg = fg).pack()
blank_label = Label(root, text="",  bg = bg, fg = fg).pack()
e1 = Entry(frame, width=45,  bg = bg, fg = fg)
e1.pack()

blank_label = Label(root, text="",  bg = bg, fg = fg).pack()
blank_label = Label(root, text="",  bg = bg, fg = fg).pack()

btn = Button(frame, text="Download Audio", command=download,  bg = bg, fg = fg).pack()
blank_label = Label(root, text="",  bg = bg, fg = fg).pack()
exit_btn = Button(frame, text="Exit", command=exit_tool,  bg = bg, fg = fg).pack()


root.mainloop()
