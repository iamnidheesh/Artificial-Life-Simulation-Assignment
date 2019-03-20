from ball import ball
from agent import agent
from follower import follower
import random
import math
from tkinter import *
from followList import followList
from followList import followList1


gui = Tk()
gui.geometry("800x800")
c = Canvas(gui,width = 800,height = 800)
c.pack()

b1 = ball(100,100,20,c,2,400,'blue',False,False,False,False,100,100)
numOfAgents = 4
for _ in range(0,numOfAgents) :
	xcord = random.randint(10,700)
	ycord = random.randint(10,700)
	followList.append(follower(xcord,ycord,20,c,2,'red'))

followList[0].follows = b1.oval
b1.agentFun()
followList[0].agentFun()
for i in range(1,numOfAgents) :
	followList[i].follows = followList[i-1].oval
	followList[i].agentFun()


#--------------------------------
b2 = ball(100,100,20,c,2,400,'pink',True,True,False,False,500,100)
for _ in range(0,numOfAgents) :
	xcord = random.randint(10,700)
	ycord = random.randint(10,700)
	followList1.append(follower(xcord,ycord,20,c,2,'yellow'))

followList1[0].follows = b2.oval
b2.agentFun()
followList1[0].agentFun()
for i in range(1,numOfAgents) :
	followList1[i].follows = followList1[i-1].oval
	followList1[i].agentFun()

gui.mainloop()
