from graphics import *
def main():

    '''点的函数'''
    win=GraphWin("Draw a polygon",300,300)
    win.setCoords(0.0,0.0,300.0,300.0)
    message=Text(Point(150,20),"Click on file points ")
    message.draw(win)
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    p4=win.getMouse()
    p4.draw(win)
    p5=win.getMouse()
    p5.draw(win)

    '''图形补充'''
    polygon = Polygon(p1, p2, p3, p4, p5)
    polygon.setFill("peachpuff")
    polygon.setFill("black")
    polygon.draw(win)
    message.setText("Click anywhere to quit.")
    win.getMouse()
if __name__ == '__main__':
    main()
