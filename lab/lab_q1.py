from tkinter import *
from ball import ball

gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,bg = 'white',width = 800,height = 800)
c.pack()
b1 = ball(100,100,20,c,5,400,'blue',False,False,False,False,100,100)
b1.agentFun()

gui.mainloop()


