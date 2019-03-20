from tkinter import *
from ball import ball
import agents
gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,bg = 'white',width = 800,height = 800)
c.pack()

agentsList = agents.makeAgents(c,40,10)
def update() :
	for i in agentsList:
		i.agentFun()
	c.after(100,update)

update()
gui.mainloop()


