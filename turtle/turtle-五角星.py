import turtle
turtle.begin_fill()
#count为绘制图形边数
turtle.pensize(12)
count=1
cs=['red','orange','yellow','green','cyan']
while count<=5:
    c=cs[count-1]
    #用指定颜色绘制每条边的颜色
    turtle.color(c)
    turtle.forward(200)
    turtle.right(144)
    count+=1
    #往整个图形填充红色
    turtle.fillcolor('red')
turtle.write('小郑画的')
turtle.end_fill()