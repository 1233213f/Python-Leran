for i in range(1,1200):# //运算次数 DARTS=1200
    x,y = random(),random()#  //生成点坐标位置
    dist = sqrt(x**2 + y**2)#  //计算此点与坐标轴原点(即圆心)的距离
    if dist <=1.0:#//与原点的距离小1,即在圆的半径内.该点落在单位圆内.
        hits = hits + 1#//落在圆内的点数合计
        pi = 4 * (hits/DARTS)
