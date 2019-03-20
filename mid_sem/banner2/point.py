class point :

	def __init__(self,x,y,vx,vy,canvas,size) :
		
		self.oldx = x-vx
		self.oldy = y-vy
		self.x = x
		self.y = y
		self.size = size
		self.canvas = canvas
		self.shape = canvas.create_oval(x,y,x+size,y+size,fill = 'black')

		
