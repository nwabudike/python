import time
import tkinter.messagebox
from tkinter import *
from plyer import notification

root = Tk()
root.geometry('400x300')
root.title('my countdown clock')

h_entry = IntVar()
m_entry = IntVar()
s_entry = IntVar()


def start_timer():
    try:
        timer_time = int(h_entry.get()) * 3600 + int(m_entry.get()) * 60 + int(s_entry.get())
    except:
        tkinter.messagebox.showerror(message='Invalid Time entered')

    if timer_time > 0:
        hour = 0
        minute = 0
        second = 0

        while timer_time >= 0:
            minute, second = divmod(timer_time, 60)
            if timer_time >= 60:
                hour, minute = divmod(timer_time, 60)

            h_entry.set(hour)
            m_entry.set(minute)
            s_entry.set(second)

            time.sleep(1)
            root.update()
            timer_time -= 1
        notification.notify(
            title='TIME ALERT',
            message='''hey hillary 
did you do what you wanted to do, if not sat another to do it again''',
            timeout=20
        )
        tkinter.messagebox.showinfo(message='Timer complete')


Label(root, text='Hillary countdown app', font='arial 15 bold').pack()
Label(root, text='Hour', font='arial 10 bold').place(x=70, y=50)
Label(root, text='Minute', font='arial 10 bold').place(x=140, y=50)
Label(root, text='Second', font='arial 10 bold').place(x=210, y=50)
Entry(root, textvariable=h_entry, width=5).place(x=70, y=80)
Entry(root, textvariable=m_entry, width=5).place(x=140, y=80)
Entry(root, textvariable=s_entry, width=5).place(x=210, y=80)

Button(root, text='Activate Timer', command=start_timer, font='arial 12', fg='black', bg='red').place(x=120, y=160)

root.mainloop()
