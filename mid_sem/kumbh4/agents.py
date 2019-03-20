
import ball
import random
agentList = []
openingx = 400
openingy = (200,600)

def makeAgents(canvas,indensity,size) :

	for _ in range(indensity) :
		xpos = random.randint(100,350)
		ypos = random.randint(100,700)
		t = 1
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))

	for _ in range(indensity) :
		xpos = random.randint(100,350)
		ypos = random.randint(100,700)
		t = 2
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))

	for _ in range(indensity) :
		xpos = random.randint(100,350)
		ypos = random.randint(100,700)
		t = 3
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))

	return agentList			


def createGates(canvas,x1,y1,x2,y2) :

	return canvas.create_line(x1,y1,x2,y2,fill = 'black')
import time

seconds = time.time()