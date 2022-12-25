import pygame as pg
from pygame import mixer
import os
from tkinter import *


root=Tk()
root.geometry('420x250')
root.title('hillary music player')

playlist = Listbox(root,selectmode=SINGLE,width=55,font='arial 10')
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\Hp\PycharmProjects\pythonProject\beginning\music_player\music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
mixer.init()
songstatus=StringVar()
songstatus.set('choosing')

def play_sound():
    currentsong=playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    songstatus.set('playing')
    mixer.music.play()
def resume_sound():
    mixer.music.unpause()
    songstatus.set('resume')

def stop_song():
    mixer.music.stop()
    songstatus.set('stopped')
def pause_song():
    mixer.music.pause()
    songstatus.set('paused')


playbtn=Button(root,text='Play',command=play_sound,font='arial 12 bold')
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text='Pause',command=pause_song,font='arial 12 bold')
pausebtn.grid(row=1,column=1)

resumebtn=Button(root,text='Resume',command=resume_sound,font='arial 12 bold')
resumebtn.grid(row=1,column=2)

stopbtn=Button(root,text='Stop',command=stop_song,font='arial 12 bold')
stopbtn.grid(row=1,column=3)









root.mainloop()