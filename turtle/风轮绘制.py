#风轮绘制
import turtle as t
t.setup()
t.pensize(5)
for i in range(4):
    t.fd(150)#直线150
    t.right(90)#转90度
    t.circle(-150,360/8)#顺时针以-150为半径，角度360/8画弧度
    t.right(90)#画完弧度后右转
    t.fd(150)#行进150回到原点
    t.right(45)
t.done()
