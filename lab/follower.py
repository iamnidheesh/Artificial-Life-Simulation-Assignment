from agent import agent
import math
from followList import followList
class follower(agent) :

	def __init__(self,startx,starty,size,canvas,velocity,color) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.velocity = velocity
		self.size = size
		self.color = color
		self.angle = 0
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = self.color)
		self.follows = 0
	
	def findAngle(self,pos,posF) :

		dy = posF[1] - pos[1]
		dx = posF[0] - pos[0]
		return math.atan2(dy,dx);

	def agentFun(self) :

		
		pos = self.canvas.coords(self.oval)
		posF = self.canvas.coords(self.follows)
		self.angle = self.findAngle(pos,posF)
		xdis = math.cos(self.angle)*self.velocity
		ydis = math.sin(self.angle)*self.velocity
		#flag = True
		"""for i in followList :
			if(i != self) :
				other = self.canvas.coords(i.oval)
				if(abs(pos[0] - other[0]) < 1.2*self.size and abs(pos[1]-other[1]) < 1.2*self.size ) :
					flag = False
					break
"""
		if(not (abs(pos[0] - posF[0]) < 1.2*self.size and abs(pos[1]-posF[1]) < 1.2*self.size)) :
		#if(flag) :
			self.canvas.move(self.oval,xdis,ydis)
		self.canvas.after(30,self.agentFun)

	



