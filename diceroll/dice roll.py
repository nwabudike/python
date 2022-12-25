from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

root.title('dice rolling')
root.geometry('400x400')
heading = Label(root, text='Dice rolling by Hillary', fg='white', bg='blue')
heading.pack()

images = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png',
          'dice6.png', ]
pickedimage = ImageTk.PhotoImage(Image.open(random.choice(images)))

pickedimagelabel = Label(root, image=pickedimage)
pickedimagelabel.image = pickedimage
pickedimagelabel.pack(expand=True)


def roll_the_dice():
    pickedimage = ImageTk.PhotoImage(Image.open(random.choice(images)))
    pickedimagelabel.configure(image=pickedimage)
    pickedimagelabel.image = pickedimage


Button = Button(root, text='roll the dice,play again', fg='red', bg='blue', command=roll_the_dice)
Button.pack()
root.mainloop()
