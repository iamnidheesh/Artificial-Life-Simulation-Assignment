from tkinter import *
from point import point
from stick import stick
import math
import time

def initialise() :
	

	for i in range(200,400,20) :
		for j in range(200,400,20) :
			points.append(point(j,i,0,0,c,5))

	#clamps.append(points[0])
	#clamps.append(points[5])
	#clamps.append(points[9])
	for i in range(0,10,3) :
		clamps.append(points[i])

	k = 10
	for i in range(0,len(points)) :

		if(i%k != 0) :
			sticks.append(stick(points[i-1],points[i],distance(points[i-1],points[i]),c))

	for i in range(10,len(points)) :
		sticks.append(stick(points[i-k],points[i],distance(points[i-k],points[i]),c))

def windSource() :

	fans[c.create_oval(100,300,100+20,300+20,fill = 'red')] = [0,False]
	fans[c.create_oval(300,100,300+20,100+20,fill = 'red')] = [1,False]
	fans[c.create_oval(500,300,500+20,300+20,fill = 'red')] = [2,False]
	fans[c.create_oval(300,500,300+20,500+20,fill = 'red')] = [3,False]



def distance(p1,p2) :

	return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

def updatePoints() :

	for p in points :

		if(p in clamps) :
			continue

		vx = p.x-p.oldx
		vy = p.y-p.oldy
		
		p.oldx = p.x
		p.oldy = p.y
		p.x += vx
		p.y += vy
		p.y += gravity

		f = list(fans.values())
		if(f[0][1]) :
			p.x += (500-p.x)*force
		if(f[1][1]) :
			p.y += (500-p.y)*force
		if(f[2][1]) :
			p.x -= (p.x-100)*force
		if(f[3][1]) :
			p.y -= (p.y-100)*force

		if(p.x > 700) :
			p.x = 700
			p.oldx = p.x + vx*bounce
		elif (p.x < 0) :
			p.x = 0
			p.oldx = p.x + vx*bounce
		if(p.y > 700) :
			p.y = 700
			p.oldy = p.y + vy*bounce
		elif(p.y < 0) :
			p.y = 0
			p.oldy = p.y + vy*bounce

def renderPoints() :

	for p in points :

 		c.coords(p.shape,p.x,p.y,p.x+p.size,p.y+p.size) 

def updateSticks() :

	for s in sticks :

		dx = s.p2.x - s.p1.x
		dy = s.p2.y - s.p1.y
		distance = math.sqrt(dx*dx + dy*dy)
		difference = s.length -distance
		if(distance != 0) :
			percent = difference/distance/2
		else :
			percent = 0
		offsetX = dx*percent
		offsetY = dy*percent

		if(s.p1 not in clamps) :
			s.p1.x -= offsetX
			s.p1.y -= offsetY
		else :
			s.p2.x += 2*offsetX
			s.p2.y += 2*offsetY

		if(s.p2 not in clamps) :
			s.p2.x += offsetX
			s.p2.y += offsetY
		else :
			s.p1.x -= 2*offsetX
			s.p1.y -= 2*offsetY


def renderSticks() :

	for s in sticks :
		c.coords(s.shape,s.p1.x + s.p1.size/2,s.p1.y+s.p1.size/2,s.p2.x+s.p2.size/2,s.p2.y+s.p2.size/2)
		
def update() :
	global ct
	if(ct%66 == 0 and len(clamps) != 0) :
		clamps.pop(0)
	updatePoints()	
	updateSticks()
	renderPoints()
	renderSticks()	
	#time.sleep(0.5)
	ct += 1
	c.after(30,update)		

def click(event) :
	if c.find_withtag(CURRENT) :
		tag = c.find_withtag(CURRENT)[0]
		if(tag in fans) :
			if(fans[tag][1]) :
				c.itemconfig(CURRENT, fill="red")
			else :
				c.itemconfig(CURRENT, fill="green")

			fans[tag][1] = not fans[tag][1]
			c.update_idletasks()

points = []
sticks = []
clamps = []
fans = {}
ct = 0
gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,bg = 'white',width = 700,height = 700)
c.pack()
gravity = 0.5
bounce = 0.9
force = 0.001
initialise()
windSource()
update()
c.bind("<Button-1>", click)
gui.mainloop()


