from agent import agent
from tkinter import *
import math

class ball(agent) :

	def __init__(self,startx,starty,size,canvas,velocity,side,f1,f2,f3,f4,posx,posy) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.velocity = velocity
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = 'blue' )
		self.side = side
		self.f1 = f1
		self.f2 = f2
		self.f3 = f3
		self.f4 = f4
		canvas.move(self.oval,posx-startx,posy-starty)

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
b1 = ball(200,200,20,c,2,200,False,False,False,False,200,200)
b2 = ball(200,200,20,c,2,200,True,False,False,False,400,200)
b3 = ball(200,200,20,c,2,200,True,True,False,False,400,400)
b4 = ball(200,200,20,c,2,200,True,True,True,False,200,400)
b1.agentFun()
b2.agentFun()
b3.agentFun()
b4.agentFun()


gui.mainloop()


