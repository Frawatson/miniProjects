from tkinter import *
import datetime
import time
import winsound

def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        currentTime = datetime.datetime.now()
        now = currentTime.strftime("%H: %M") #%S")
        date = currentTime.strftime("%d/%m/%y")
        print("The set date is: ", date)
        print(now)
        if(now == setAlarmTimer):
            print("Time to wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break
def actualTIme():
    setAlaramTimer = f"{hour.get()}: {min.get()}" #{sec.get()}"
    alarm(setAlaramTimer)

clock=Tk()

clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text= "Enter time in 24 hours format", fg="red", bg="black", font="Ariel").place(x=60, y=120)
addTime = Label(clock, text = " Hour Min", font = 60).place(x = 110)
setYourAlarm = Label(clock, text = "Wake up time", fg="blue", relief = "solid", font = ("Helevetica", 7, "bold")).place(x = 0, y=29)

hour = StringVar()
min = StringVar()
#sec = StringVar()

hourTime = Entry(clock, textvariable = hour, bg = "green", width = 15).place(x = 110, y=30)
minTime = Entry(clock, textvariable = hour, bg = "green", width = 15).place(x = 150, y=30)
#secTime = Entry(clock, textvariable = hour, bg = "green", width = 15).place(x = 200, y=30)

submit = Button(clock, text = "Set Alarm", fg="red", width = 10, command = actualTIme).place(x = 110, y = 70)

clock.mainloop()