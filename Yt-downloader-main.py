# importing modules
from fileinput import filename
from pytube import YouTube
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Create an instance of tkinter frame or window
window = Tk()

text = StringVar(window, value='Type YouTube URL Here')
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
res4 = IntVar()


def downloader():  # defining a function
    global res  # global variable
    t = text.get()  # getting the value
    video = YouTube(t)

    if res1.get() == 18:
        res = 18
    elif res2.get() == 22:
        res = 22
    elif res3.get() == 137:
        res = 137
    elif res4.get() == 140:
        res = 140

    mp4_file = video.streams.filter(file_extension='mp4').get_by_itag(res)
    mp4_file.download(filename=None, output_path="E:\\pritam\\YT_downloads")
    messagebox.showinfo("Downloaded", "Downloaded Successfully")


# Set the size of the tkinter window
window.geometry("700x350")
root = tk.Tk()
root.iconbitmap("myIcon.ico")
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
Checkbutton(text='1080p', onvalue=137, offvalue=0,
            variable=res3).pack()  # creating checkbox
Checkbutton(text='Convert to Audio', onvalue=140,
            offvalue=0, variable=res4).pack()
# creating a button
Button(window, text="Download", bg='red', command=downloader).pack()

window.mainloop()
