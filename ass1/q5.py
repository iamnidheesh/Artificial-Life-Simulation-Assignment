from agent import agent
from tkinter import *
import math
import numpy as np

class ball(agent) :

	def __init__(self,startx,starty,size,x1,y1,x2,y2,x3,y3,canvas,velocity,f1,f2,f3,posx,posy) :
		self.startx = startx
		self.starty = starty
		self.size = size
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.angle1 = math.atan2((y2-y1),(x2-x1))
		self.angle2 = math.atan2((y3-y2),(x3-x2))
		self.angle3 = math.atan2((y1-y3),(x1-x3))
		self.canvas = canvas
		self.velocity = velocity
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = 'blue' )
		self.f1 = f1
		self.f2 = f2
		self.f3 = f3
		self.canvas.move(self.oval,posx-startx,posy-starty)


	def agentFun(self) :

		xdis = 0
		ydis = 0
		pos = self.canvas.coords(self.oval)
	
		if(not self.f1) :
			xdis = math.cos(self.angle1)*self.velocity
			ydis = math.sin(self.angle1)*self.velocity
			if(abs(pos[0]-self.x2) < self.velocity and abs(pos[1]-self.y2) < self.velocity ) :
				self.f1 = True

		elif(not self.f2) :
			xdis = math.cos(self.angle2)*self.velocity
			ydis = math.sin(self.angle2)*self.velocity
			if(abs(pos[0]-self.x3) < self.velocity and abs(pos[1]-self.y3) < self.velocity ) :
				self.f2 = True

		elif(not self.f3) :
			xdis = math.cos(self.angle3)*self.velocity
			ydis = math.sin(self.angle3)*self.velocity
			if(abs(pos[0]-self.x1) < self.velocity and abs(pos[1]-self.y1) < self.velocity ) :
				self.f3 = True

		self.canvas.move(self.oval,xdis,ydis)
		if(self.f1 and self.f2 and self.f3 ) :
			
			self.f1 = False
			self.f2 = False
			self.f3 = False
		self.canvas.after(30,self.agentFun)


gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,width = 800,height = 800)
c.pack()
b1 = ball(200,200,20,200,200,300,400,50,300,c,3,False,False,False,200,200)
b2 = ball(200,200,20,200,200,300,400,50,300,c,3,True,False,False,300,400)
b3 = ball(200,200,20,200,200,300,400,50,300,c,3,True,True,False,50,300)

b1.agentFun()
b2.agentFun()
b3.agentFun()


gui.mainloop()


