from graphics import *
p1=Point(100,100)
p1.getX()
p2=Point(150,80)
win=GraphWin()
p1.draw(win)
p2.draw(win)
win.getMouse() # pause for click in window
win.close()