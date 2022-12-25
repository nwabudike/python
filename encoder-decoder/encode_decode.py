from tkinter import *
import base64

root = Tk()
root.geometry('400x400')

# create variables that stores the display values
text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()


def Encode(key, message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return ''.join(dec)


def Result():
    if (mode.get() == 'e'):
        result.set(Encode(private_key.get(), text.get()))
    elif (mode.get() == 'd'):
        result.set(Decode(private_key.get(), text.get()))
    else:
        result.set('Invalid Mode')


def Exit():
    root.destroy()


def reset():
    text.set('')
    private_key.set('')
    mode.set('')
    result.set('')


Label(root, text='ENCODE DECODE', font='arial 12 bold', fg='white', bg='red').pack()

Label(root, text='MESSAGE', font='arial 12 bold').place(x=40, y=60)
Entry(root, font='arial 10', textvariable=text).place(x=190, y=60)

Label(root, text='KEY', font='arial 12 bold').place(x=40, y=90)
Entry(root, font='arial 10', textvariable=private_key).place(x=190, y=90)

Label(root, text='Mode,e-encoder d-decoder', font='arial 12 bold').place(x=40, y=120)
Entry(root, font='arial 10', textvariable=mode).place(x=250, y=120)

Button(root, text='Result', font='arial 12 bold', command=Result).place(x=40, y=150)
Entry(root, font='arial 10', textvariable=result).place(x=190, y=160)

Button(root, text='Reset', font='arial 12 bold', command=reset).place(x=80, y=190)

Button(root, text='Exit', font='arial 12 bold', command=Exit).place(x=180, y=190)

root.mainloop()
