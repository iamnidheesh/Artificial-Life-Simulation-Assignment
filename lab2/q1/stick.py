import math
class stick :


	def __init__(self,p1,p2,length,canvas) :
		
		self.p1 = p1
		self.p2 = p2
		self.length = length
		self.canvas = canvas
		self.shape = canvas.create_line(p1.x,p1.y,p2.x,p2.y,fill = 'black')

	