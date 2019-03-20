from tkinter import *
import ball
import agents
import random

def update() :

	for i in agentsList:
		i.agentFun()
	
	c.after(30,update)






gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,bg = 'white',width = 800,height = 800)
c.pack()
indensity = 5
outdensity = 5
agentsList = agents.makeAgents(c,indensity,outdensity,10)
gate1 = agents.createGates(c,400,0,400,200)
gate2 = agents.createGates(c,400,800,400,600)
update()
gui.mainloop()


