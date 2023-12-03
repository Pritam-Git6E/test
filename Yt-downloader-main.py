        # importing modules
from importlib.resources import path
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from fileinput import filename
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox



# Create an instance of tkinter frame or window
window = Tk()

#define Variables for resolution 
text = StringVar(window, value='Type YouTube URL Here')
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
res4 = IntVar()

#define Directory where file Will be saved 
def chooseDir():
    global path
    path = filedialog.askdirectory(title="Choose a download directory")
    tk.Label(window, text=path, bg='gray').place(x=240,y=300)
    
#define download Function
def downloader():  # defining a function
    global res  # global variable
    t = text.get()  # getting the value
    video = YouTube(t)

    if res1.get() == 18:
        res = 18
    elif res2.get() == 22:
        res = 22
    elif res3.get() == 394:
        res = 394
    elif res4.get() == 140:
        res = 140

    mp4_file = video.streams.filter(file_extension='mp4').get_by_itag(res)
    mp4_file.download(str(path))
    messagebox.showinfo("Downloaded", "Downloaded Successfully")
    window.update_idletasks()

# def download_audio():
#     global res
#     a = text.get()  # getting the value
#     audio = YouTube(a)
#     if res4.get() == 250:
#         res4 = 250


#     mp3_file = audio.streams.filter(only_audio=True, file_extension="mp3").get_by_itag(res)
#     mp3_file.download(str(path))
#     messagebox.showinfo("Downloaded", "Downloaded Successfully")


window.geometry("700x350")
window.config(bg="#e8e8e8")

# give title to the window
window.title("Youtube Downloader")

Label(window, text="YOUTUBE VIDEO DOWNLOADER",
      bg='grey', font=('Calibri 15')).pack()  # a label
Label(window, text="Enter the link to download",
      font=('Calibri 12')).pack()  # a label

Entry(window, textvariable=text, width=50).pack()  # entry field
Checkbutton(text='360p', onvalue=18, offvalue=0,
            variable=res1).pack()  # creating checkbox
Checkbutton(text='720p', onvalue=22, offvalue=0,
            variable=res2).pack()  # creating checkbox
Checkbutton(text='1080p', onvalue=394, offvalue=0,
            variable=res3).pack()  # creating checkbox
Checkbutton(text='Convert to Audio', onvalue=140,
            offvalue=0, variable=res4).pack()
Button(window, text='Browse', command= chooseDir,  bg="green").pack(padx=10, pady= 5)

# creating a button
Button(window, text="Download", bg='red', command=downloader).pack()
# Button(window, text="Download", bg='red', command=download_audio).pack()

window.mainloop()
