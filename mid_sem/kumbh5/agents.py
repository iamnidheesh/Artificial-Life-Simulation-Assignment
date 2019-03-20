
import ball
import random
agentList = []


def makeAgents(canvas,indensity,outdensity,size) :

	for _ in range(indensity) :
		xpos = random.randint(100,350)
		ypos = random.randint(100,700)
		t = 1
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))

	for _ in range(outdensity) :
		xpos = random.randint(450,700)
		ypos = random.randint(100,700)
		t = 2
		agentList.append(ball.ball(xpos,ypos,size,canvas,0,t))	

	return agentList			


