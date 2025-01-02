# import Required Library

from tkinter import *
import datetime
import time
import winsound
from threading import *

#create Object
 
root = Tk()
root.geometry("400x400")

# Set background color to black
root.config(bg="black")


# USE Threading

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        # to set a alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
       
       # wait for a sec which makes reduce of enegy in CPU
        time.sleep(1)

        #GET CURRENT TIME
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)


        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to wake up")
         # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("poppins 30 bold"), fg="red" , bg="black").pack(pady=15)
Label(root, text="Set Time", font=("sans-sherif 20 bold"),fg="white" , bg="black").pack(padx=10,pady=5)

frame = Frame(root, bg="black")
frame.pack(pady=5)

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.config(bg="black", fg="white")
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.config(bg="black", fg="white")
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.config(bg="black", fg="white")
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"),bg="black", fg="red", command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()