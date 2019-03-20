
from agents import agentList,openingx,openingy,seconds
import math
import random

class ball :

	
	def assignColor(self,t) :
		if(t == 1) :
			return 'blue'
		elif(t == 2) :
			return 'red'
		else:
			return 'grey'

	def attraction(self,other,constant) :

		pos = self.canvas.coords(self.shape)
		posH = self.canvas.coords(other.shape)
		xdis = (posH[0]+posH[2]-pos[0]-pos[2])/2 - self.size
		ydis = (posH[1]+posH[3]-pos[1]-pos[3])/2 - self.size
		dis = math.sqrt(xdis**2 + ydis**2 )
		
		return (constant*dis*xdis,constant*dis*ydis)


	def repulsion(self,other,constant) :

		pos = self.canvas.coords(self.shape)
		posH = self.canvas.coords(other.shape)
		xdis = (posH[0]+posH[2]-pos[0]-pos[2])/2 - self.size
		ydis = (posH[1]+posH[3]-pos[1]-pos[3])/2 - self.size
		dis = math.sqrt(xdis**2 + ydis**2 )
		return (-constant*xdis/(10**-18 + dis*dis*dis),-constant*ydis/(10**-18 + dis*dis*dis))

	def gateA(self,ox,oy,constant):
		pos = self.canvas.coords(self.shape)
		xdis = ox - (pos[0]+pos[2])/2
		ydis = oy - (pos[1]+pos[3])/2 
		dis = math.sqrt(xdis**2 + ydis**2)

		return (constant*dis*xdis,constant*dis*ydis)

	def gateR(self,ox,oy,constant):
		pos = self.canvas.coords(self.shape)
		xdis = ox - (pos[0]+pos[2])/2 
		ydis = oy - (pos[1]+pos[3])/2 
		dis = math.sqrt(xdis**2 + ydis**2)

		return (-constant*xdis/(10**-18+ dis*dis*dis),-constant*ydis/(10**-18 + dis*dis*dis))

	def __init__(self,startx,starty,size,canvas,velocity,t) :
		self.startx = startx
		self.starty = starty
		self.canvas = canvas
		self.velocity = velocity
		self.angle = 0
		self.size = size
		self.t = t
		self.shape = canvas.create_oval(startx,starty,startx+size,starty+size,fill = self.assignColor(self.t))
	
	def agentFun(self) :

		xdis = 0
		ydis = 0
		posForce = [0,0]
		negForce = [0,0]

		#Social potential
		for i in agentList :
				if(i == self) :
					continue

				if(i.t == self.t) :
					forcea = self.attraction(i,10**-7)
					forcer = self.repulsion(i,10**2)
					posForce[0] += forcea[0] + forcer[0]
					posForce[1] += forcea[1] + forcer[1]
				else :
					forcea = self.attraction(i,10**-7)
					forcer = self.repulsion(i,10**1)
					negForce[0] += forcea[0] + forcer[0]
					negForce[1] += forcea[1] + forcer[1]

		# Towards gate
		pos = self.canvas.coords(self.shape)
		ox = openingx
		oy = openingy[1]-openingy[0]
		extraForce = (0,0)
		ex = 0
		if((pos[0] < ox-20) ) :

			extraForce = self.gateA(ox,openingy[0] + oy/3,(4-self.t)*10**-4)  #+ self.gateR(ox,openingy[0] + oy/3,1)

		else:
			ox = 800
			oy = self.starty
			extraForce = self.gateA(ox,oy,(4-self.t)*10**-4) #+ self.gateR(ox,oy,10)
		
		if(self.t == 1) :
			ex = 0.4
		elif(self.t == 2) :
			ex = 0.05
		else :
			ex = 0.005
		
		xdis =  posForce[0] + negForce[0] + extraForce[0] + ex
		ydis =  posForce[1] + negForce[1] + extraForce[1]
		if(pos[0]+xdis <= 0 or pos[0]+xdis >= 800 or pos[1] + ydis >= 800 or pos[1] + ydis <= 0) :
			agentList.remove(self)
			self.canvas.delete(self.shape)
		else :
		
			if(pos[0] < openingx and pos[0]+xdis > openingx) :
				if(pos[1] + ydis > openingy[0] and pos[1] + ydis < openingy[1]) :
					self.canvas.move(self.shape,xdis,ydis)
				else :
					if(pos[1] + ydis <= openingy[0]) :
						ydis += 0.1
						self.canvas.move(self.shape,0,ydis)

					else :
						ydis -= 0.1
						self.canvas.move(self.shape,0,ydis)


			else :		
				self.canvas.move(self.shape,xdis,ydis)
			