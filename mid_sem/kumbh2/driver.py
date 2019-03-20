from tkinter import *
import ball
import agents
import random

def update() :
	global ct
	if(ct%33 == 0) :
		for i in range(2) :
			xpos = random.randint(100,350)
			ypos = random.randint(100,700)
			agents.agentList.append(ball.ball(xpos,ypos,10,c,0,1))
		for i in range(2) :
			xpos = random.randint(450,700)
			ypos = random.randint(100,700)
			agents.agentList.append(ball.ball(xpos,ypos,10,c,0,2))

	for i in agentsList:
		i.agentFun()
	ct += 1
	c.after(30,update)






gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,bg = 'white',width = 800,height = 800)
c.pack()
ct = 0
indensity = 5
outdensity = 5
agentsList = agents.makeAgents(c,indensity,outdensity,10)
gate1 = agents.createGates(c,400,0,400,200)
gate2 = agents.createGates(c,400,800,400,600)
update()
gui.mainloop()


