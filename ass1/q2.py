from agent import agent
from tkinter import *
import math

class ball(agent) :

	def __init__(self,startx,starty,size,canvas,velocity,side) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.velocity = velocity
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = 'blue' )
		self.side = side
		self.f1 = False
		self.f2 = False
		self.f3 = False
		self.f4 = False
	
	def agentFun(self) :

		xdis = 0
		ydis = 0
		pos = self.canvas.coords(self.oval)
		if(not self.f1) :
			xdis = self.velocity
			if(abs(self.startx - pos[0]) > self.side):
				self.f1 = True

		elif(not self.f2) :
			ydis = self.velocity
			if(abs(self.starty - pos[1]) > self.side):
				self.f2 = True

		elif(not self.f3) :
			xdis = -self.velocity
			if(abs(self.startx - pos[0]) < 1):
				self.f3 = True

		elif(not self.f4) :
			ydis = -self.velocity
			if(abs(self.starty - pos[1]) < 1):
				self.f4 = True

		self.canvas.move(self.oval,xdis,ydis)
		if(self.f1 and self.f2 and self.f3 and self.f4) :
			
			self.f1 = False
			self.f2 = False
			self.f3 = False
			self.f4 = False
		self.canvas.after(30,self.agentFun)


gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,width = 800,height = 800)
c.pack()
b1 = ball(200,200,20,c,5,200)
b1.agentFun()


gui.mainloop()


