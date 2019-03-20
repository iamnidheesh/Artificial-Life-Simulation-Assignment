
from agents import agentList
import math

class ball :

	
	def assignColor(self,t) :
		if(t == 1) :
			return 'black'
		elif(t == 2) :
			return 'red'
		else:
			return 'grey'

	def attraction(self,other,constant) :

		pos = self.canvas.coords(self.shape)
		posH = self.canvas.coords(other.shape)
		dis = math.sqrt((posH[0]-pos[0])**2 + (posH[1]-pos[1])**2 )
		xdis = posH[0]-pos[0]
		ydis = posH[1]-pos[1]
	
		return (constant*dis*xdis,constant*dis*ydis)


	def repulsion(self,other,constant) :

		pos = self.canvas.coords(self.shape)
		posH = self.canvas.coords(other.shape)
		dis = math.sqrt((posH[0]-pos[0])**2 + (posH[1]-pos[1])**2 )
		xdis = posH[0]-pos[0]
		ydis = posH[1]-pos[1]
		
		return (-constant*xdis/(1 + dis*dis*dis),-constant*ydis/(1 + dis*dis*dis))

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
		posForce = 0
		negForce = 0
		#pos = self.canvas.coords(self.oval)
		for i in agentList :
				if(i == self) :
					continue
				if(i.t == self.t) :
					posForce = self.attraction(i,10**-4) + self.repulsion(i,10**-7)
				else :
					negForce = self.repulsion(i,10**-4) + self.attraction(i,10**-7)

		xdis =  posForce[0] + negForce[0]
		ydis =  posForce[1] + negForce[1]
		self.angle = math.atan2(xdis,ydis)
		self.canvas.move(self.shape,xdis,ydis)
