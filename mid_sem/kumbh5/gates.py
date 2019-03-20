def createGates(canvas,x1,y1,x2,y2) :

	return canvas.create_line(x1,y1,x2,y2,fill = 'black')


from canvas import c
gate1 = createGates(c,400,0,400,200)
gate2 = createGates(c,400,800,400,600)
