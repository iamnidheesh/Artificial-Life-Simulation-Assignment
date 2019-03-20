
import ball
import random
agentList = []

def makeAgents(canvas,num,size) :

	for _ in range(num) :
		xpos = random.randint(100,700)
		ypos = random.randint(100,700)
		t = (xpos+ypos)%3
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))

	return agentList			


