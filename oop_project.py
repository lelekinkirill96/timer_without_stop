from tkinter import *
from playsound import playsound
import time

class Timer:
    def __init__(self):
        self.h = 00
        self.min = 00
        self.sec = 00
        self.root = Tk()
        self.root.title('Timer')
        self.root.config(bg='white')
        self.root.geometry('380x300+100+100')
        self.title = Label(
            self.root,
            text='Timer',
            font=('Arial 16 bold'),
            bg='brown',
            fg='#FF0')
        self.title.place(x = 150, y = 10)

        self.hours = StringVar(self.root)
        self.hours_inp = Entry(self.root, textvariable=self.hours, width=2, font='arial 50', bg='white', fg='black', bd=0)
        self.hours.set('00')
        self.minutes = StringVar(self.root)
        self.minutes_inp = Entry(self.root, textvariable=self.minutes, width=2, font='arial 50', bg='white', fg='black', bd=0)
        self.minutes.set('00')
        self.seconds = StringVar(self.root)
        self.seconds_inp = Entry(self.root, textvariable=self.seconds, width=2, font='arial 50', bg='white', fg='black', bd=0)
        self.seconds.set('00')
        self.hours_inp.place(x = 30, y = 100)
        self.title = Label(
            self.root,
            text=':',
            font=('Arial 50 bold'),
            bg='white',
            fg='black')
        self.title.place(x=115, y=90)
        self.minutes_inp.place(x=150, y=100)
        self.title = Label(
            self.root,
            text=':',
            font=('Arial 50 bold'),
            bg='white',
            fg='black')
        self.title.place(x=235, y=90)
        self.seconds_inp.place(x=270, y=100)

        self.start = Button(self.root, text='start', font=('Arial', 12), bg='white', command = self.timer)
        self.stop = Button(self.root, text='stop', font=('Arial', 12), bg='white', command = self.stop)

        self.start.place(x = 100, y = 200)
        self.stop.place(x = 200, y = 200)

        self.root.mainloop()
    def timer(self):
        times = int(self.hours.get())*3600 + int(self.minutes.get())*60 + int(self.seconds.get())
        while times > -1:
            self.min, self.sec = (times//60, times%60)
            self.h = 0
            if self.min > 60:
                self.h, self.min = (self.min // 60, self.min % 60)
            self.hours.set(self.h)
            self.minutes.set(self.min)
            self.seconds.set(self.sec)
            self.root.update()
            time.sleep(1)
            times -= 1

    def stop(self):
        self.h = 00
        self.min = 00
        self.sec = 00
        self.seconds.set(self.sec)
        self.minutes.set(self.min)
        self.hours.set(self.h)
        self.root.update()
n = Timer()