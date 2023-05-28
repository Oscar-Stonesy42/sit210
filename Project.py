from gpiozero import LightSensor
from tkinter import *
import tkinter as tk
import tkinter
import RPi.GPIO as GPIO

powerStatus = 0

#define sensor
ldr = LightSensor(4)

#define light
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

#define functions
def tripwirePower():
	global powerStatus
	switchStatus()		
	if powerStatus == 1:
		print("TURNED ON")
		ldr.when_dark = lambda: print("INTRUDER")
	elif powerStatus == 0:
		print("TURNED OFF")
		ldr.when_dark = lambda: print(" ")

def switchStatus():
	global powerStatus
	if powerStatus == 0:
		powerStatus = 1
		GPIO.output(21,GPIO.LOW)
	elif powerStatus == 1:
		powerStatus = 0
		GPIO.output(21,GPIO.HIGH)

#create window
window = tkinter.Tk()
window.minsize(200,200)
window.title("Tripwire System")
window.geometry("600x400+100+20")

#create frames
frmHeader = Frame(window)
frmBody = Frame(window)
frmFooter = Frame(window)

#pack frames
frmHeader.pack(fill=X)
frmBody.pack(fill=BOTH, expand=TRUE)
frmFooter.pack()

# creates labels/widgets
lblTitle = Label(frmHeader, text="Tripwire System", font=("Arial", 24), fg="grey")
lblDesc = Label(frmBody, text="Push the button to activate and deactivate the tripwire", font=("Arial", 18), fg="grey")

#create button
btnOn = Button(frmBody, text="Activate Tripwire", font=("Arial", 20), bg = "red", command=tripwirePower)
btnOff = Button(frmBody, text="Deactivate Tripwire", font=("Arial", 20), bg = "red", command=tripwirePower)

#pack labels/widgets
lblTitle.pack()
lblDesc.place(x=15, y=100)
btnOn.place(x=15,y=200)
btnOff.place(x=300,y=200)


#end program
window.mainloop()
