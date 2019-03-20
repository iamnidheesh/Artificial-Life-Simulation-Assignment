from agent import agent
from followList import followList

class ball(agent) :

	def __init__(self,startx,starty,size,canvas,velocity,side,color,f1,f2,f3,f4,posx,posy) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.velocity = velocity
		self.size = size
		self.color = color
		self.oval = canvas.create_oval(startx,starty,startx+size,starty+size,fill = self.color )
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
			ydis = self.velocity
			
			if(abs(self.startx - pos[0]) > self.side):
				self.f1 = True

		elif(not self.f2) :
			ydis = -self.velocity
			if(abs(self.starty - pos[1]) < 1):
				self.f2 = True

		elif(not self.f3) :
			xdis = -self.velocity
			ydis = self.velocity
			if(abs(self.startx - pos[0]) < 1):
				self.f3 = True

		elif(not self.f4) :
			ydis = -self.velocity
			if(abs(self.starty - pos[1]) < 1):
				self.f4 = True

		flag = True
		"""for i in followList :
			if(i != self) :
				other = self.canvas.coords(i.oval)
				if(abs(pos[0] - other[0]) < 1.2*self.size and abs(pos[1]-other[1]) < 1.2*self.size ) :
					flag = False
					break
					"""
		#if(flag) :		
		self.canvas.move(self.oval,xdis,ydis)
		if(self.f1 and self.f2 and self.f3 and self.f4) :
			
			self.f1 = False
			self.f2 = False
			self.f3 = False
			self.f4 = False
		self.canvas.after(30,self.agentFun)
