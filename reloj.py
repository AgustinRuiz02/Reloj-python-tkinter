from tkinter import Tk
from tkinter import Label
import time
import sys

root=Tk()
root.title("Reloj")

def tiempo():
    display_time = time.strftime("%I:%M:%S %p")
    digi_clock.config(text=display_time)
    digi_clock.after(200,tiempo)

digi_clock=Label(root, font=("arial",150), bg="#396277", fg="#C1D1D8")
digi_clock.pack()

tiempo()
root.mainloop()