from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import ttk
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()
win.title("Blink the LED")

whiteled = LED(14)

entry= Entry(win, width = 50, bg = "lavender", fg = "black")
entry.focus_set()
entry.pack()

def dash():
    whiteled.on()
    time.sleep(1.50)
    whiteled.off()
    time.sleep(0.25)

def dot():
    whiteled.on()
    time.sleep(0.75)
    whiteled.off()
    time.sleep(0.25)

def nameconverter():
    hello = entry.get()
    text = hello.upper()
    if len(hello) < 13:
        i=0
        while i < (len(hello)):
            if text[i] == 'A':
                dot()
                dash()
            if text[i] == 'B':
                dash()
                dot()
                dot()
                dot()
            if text[i] == 'C':
                dash()
                dot()
                dash() 
                dot()
            if text[i] == 'D':
                dash()
                dot() 
                dot()
            if text[i] == 'E':
                dot()
            if text[i] == 'F':
                dot() 
                dot() 
                dash() 
                dot()
            if text[i] == 'G':
                dash() 
                dash() 
                dot()
            if text[i] == 'H':
                dot() 
                dot() 
                dot()
                dot()
            if text[i] == 'I':
                dot()
                dot()
            if text[i] == 'J':
                dot()
                dash() 
                dash()
                dash()
            if text[i] == 'K':
                dash()
                dot() 
                dash()
            if text[i] == 'L':
                dot() 
                dash() 
                dot()
                dot()
            if text[i] == 'M':
                dash() 
                dash()
            if text[i] == 'N':
                dash() 
                dot()
            if text[i] == 'O':
                dash() 
                dash() 
                dash()
            if text[i] == 'P':
                dot() 
                dash() 
                dash()
                dot()
            if text[i] == 'Q':
                dash() 
                dash() 
                dot() 
                dash()
            if text[i] == 'R':
                dot() 
                dash() 
                dot()
            if text[i] == 'S':
                dot() 
                dot() 
                dot()
            if text[i] == 'T':
                dash()
            if text[i] == 'U':
                dot() 
                dot() 
                dash()
            if text[i] == 'V':
                dot() 
                dot() 
                dot() 
                dash()
            if text[i] == 'W':
                dot()
                dash() 
                dash()
            if text[i] == 'X':
                dash() 
                dot() 
                dot() 
                dash()
            if text[i] == 'Y':
                dash() 
                dot() 
                dash() 
                dash()
            if text[i] == 'Z':
                dash() 
                dash() 
                dot() 
                dot() 
            if text[i] == ' ':
                time.sleep(2)
            i = i + 1
    else:
        print("You have entered the text greater than 12 words")


def close():
    RPi.GPIO.cleanup()
    win.destroy()


button = Button(win, text = "Submit", command = nameconverter, bg = "light blue", fg = "white")
button.pack()

exitbutton = Button(win, text = "Exit", command = close, bg = "Red", fg = "white")
exitbutton.pack()

win.mainloop()
