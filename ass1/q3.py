from agent import agent
from tkinter import *
import math

class ball(agent) :

	def __init__(self,startx,starty,centerx,centery,size,canvas,radius,omega) :
		self.startx = startx
		self.starty = starty
		self.centery = centery
		self.centerx = centerx
		self.canvas = canvas
		self.radius = radius
		self.omega = omega
		self.angle = 0
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = 'blue' ) 
		self.canvas.move(self.oval,radius + centerx-startx,centery-starty)

	def agentFun(self) :
		pos = self.canvas.coords(self.oval)
		xdis = -pos[0]+self.radius*math.cos(self.angle)+self.centerx
		ydis = -pos[1]+self.radius*math.sin(self.angle)+self.centery
		self.angle += self.omega
		self.canvas.move(self.oval,xdis,ydis)
		self.canvas.after(10,self.agentFun)


gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,width = 800,height = 800)
c.pack()
b1 = ball(20,20,400,400,20,c,100,0.01)
b1.agentFun()
gui.mainloop()


