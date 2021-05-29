try:
    from tkinter import *
    from tkinter import messagebox as mb
    import os
    import platform

except Exception as e:
    print(f"[ ERROR : {e} ]  Press any key to continue...")
    exit()


try:
    os.system('pip --version')

except :
    mb.showerror('error', "Pip is not installed,install it first")
    exit()

root = Tk()
root.title("Setup - YT Downloader")
root.geometry("250x50")
root.maxsize(250, 50)
root.config(background="black")

main_label = Label(root, text = "Configuring Setup...", foreground="cyan", background="black", font=("sans 14"), pady=10).pack()

mb.showwarning("Message", "Before installing setup,make sure you have an active internet connection,python3 and pip installed!")


mb.showinfo('Downloading', "Please wait until we downloading the setup...")


os_name = platform.system()

if os_name == "Linux" or os_name == "Ubuntu":
    try :
        os.system('pip install pytube')
        os.system('pip install youtube-dl')

    except Exception as e:
        mb.showerror('error', "an error occured,please install modules manually using 'pip',listed on GitHub Repo")
        exit() 

elif os_name == "Windows" or os_name == "windows":
    try :
        os.system('cmd /k "pip install pytube"')
        os.system('cmd /k "pip install youtube-dl"')

    except Exception as e:
        mb.showerror('error', "an error occured,please install modules manually using 'pip',listed on GitHub Repo")
        exit()

else :
    mb.showerror('Error', "Sorry,this tool is not available for your OS")
    exit()

mb.showinfo('Congrats!', "Setup successfully installed in your system,now you can use YT-Downloader")

root.destroy()
root.mainloop()