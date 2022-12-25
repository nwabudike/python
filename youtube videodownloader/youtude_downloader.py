from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('400x400')
link = StringVar()
Label(root, text='Youtube Videodownloader', font='arial 12 bold', justify=CENTER).pack()

Label(root, text='Paste your link', font='arial 10 bold',).place(x=160, y=60)

Entry(root, textvariable=link, width=70,).place(x=32, y=90)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='arial 10').place(x=180, y=210)


Button(root, text='Download', font='arial 10', command=download).place(x=180, y=150)

root.mainloop()
