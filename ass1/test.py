from tkinter import *

import time

gui = Tk()

gui.geometry("400x400")

c = Canvas(gui ,width=400 ,height=400)

c.pack()

oval = c.create_oval(2.5,2.5,30,30,fill='pink')

xd = 5

yd = 10

while True:

  c.move(oval,xd,yd)

  p=c.coords(oval)

  if p[3] >= 400 or p[1] <=0:

     yd = -yd

  if p[2] >=400 or p[0] <=0:

     xd = -xd

  gui.update()

  time.sleep(0.025) 

gui.title("First title")

gui.mainloop()