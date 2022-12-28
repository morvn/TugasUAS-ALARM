from tkinter import *
import datetime
import time
import os
import winsound

def alarm(pengaturan):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Waktu Telah Diatur Pada:",date)
        print(now)
        if now == pengaturan:
            print("Waktunya Banguunnn..!!!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
        
def shutdown():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Waktu Telah Diatur Pada:", date)
        if now == f"{hour.get()}:{min.get()}:{sec.get()}":
            os.system("shutdown /s")
            break

def actual_time():
    pengaturan = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(pengaturan)

clock = Tk()
clock.title("Nave Alarm")
clock.geometry("400x200")
time_format=Label(clock, text= "Masukkan Waktu Dalam Format 24 Jam!!", fg="white",bg="black",font="Cambria").place(x=21,y=120)
addTime = Label(clock,text = "JAM | MENIT | DETIK",font=10).place(x = 105)
setYourAlarm = Label(clock,text = " Time Set ",fg="black",relief = "flat",font=("Helevetica",7)).place(x=40, y=30)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "white",width = 15).place(x=90,y=30)
minTime= Entry(clock,textvariable = min,bg = "white",width = 15).place(x=155,y=30)
secTime = Entry(clock,textvariable = sec,bg = "white",width = 15).place(x=235,y=30)

nave = Button(clock,text = "Mulai Alarm",fg="black", command = actual_time).place(x =95,y=70)
morvn = Button(clock, text="Auto Shutdown", command=shutdown).place(x =200,y =70)

clock.mainloop()
