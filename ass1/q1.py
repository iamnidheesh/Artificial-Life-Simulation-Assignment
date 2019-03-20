from agent import agent
from tkinter import *
import math

class ball(agent) :

	def __init__(self,startx,starty,size,canvas,endx,endy,velocity) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.endx = endx
		self.endy = endy
		self.velocity = velocity
		self.angle = math.atan((starty-endy)/(startx-endx))
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = 'blue' ) 
	
	def agentFun(self) :

		pos = self.canvas.coords(self.oval)
		xdis = math.cos(self.angle)*self.velocity
		ydis = math.sin(self.angle)*self.velocity
		self.canvas.move(self.oval,xdis,ydis)
		if(abs(pos[0]-self.endx) < self.velocity or abs(pos[1]-self.endy) < self.velocity ) :
			return
		self.canvas.after(10,self.agentFun)


gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,width = 800,height = 800)
c.pack()
b1 = ball(50,50,20,c,600,600,3)
b1.agentFun()

gui.mainloop()


