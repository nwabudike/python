import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry('400x400')

text = StringVar()
Label(root, text='Text_To_Speech', font='arial 15 bold').pack()
Label(root, text='Enter Text', font='arial 10 bold').place(x=10, y=60)

Entry(root, textvariable=text, width=80).place(x=10, y=90)


def Play():
    message = text.get()
    speech = gTTS(text=message)
    speech.save('message.mp3')
    playsound('message.mp3')
    os.remove('message.mp3')

def Reset():
    text.set('')



def Exit():
    root.destroy()


Button(root, text='PLAY', command=Play, font='arial 12 bold').place(x=15, y=130)
Button(root, text='RESET', command=Reset, font='arial 12 bold',bg='red').place(x=90, y=130)
Button(root, text='EXIT', command=Exit, font='arial 12 bold').place(x=165, y=130)

root.mainloop()
