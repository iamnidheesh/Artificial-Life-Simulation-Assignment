import ball
import agents
import random
import gates
import canvas
def update() :
	global ct
	for i in agentsList:
		i.agentFun()
	if(ct%33 == 0) :
		pos1 = canvas.c.coords(gates.gate1)[3]
		pos2 = canvas.c.coords(gates.gate2)[3]
		canvas.c.coords(gates.gate1,400,0,400,pos1+20)
		canvas.c.coords(gates.gate2,400,800,400,pos2-20)
	ct += 1
	canvas.c.after(30,update)


ct = 0
indensity = 20
outdensity = 10
agentsList = agents.makeAgents(canvas.c,indensity,outdensity,10)

update()
canvas.gui.mainloop()


