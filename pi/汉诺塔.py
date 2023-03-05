count=0
def hanoi(n,start,mid,aim):#参数位置1-4对应：圆环数量，搬动起点，搬动中间位置，搬动终点,
    global count
    if n==1:
        print('{}:{}->{}'.format(1,start,aim))
        count+=1
    else:
        hanoi(n-1,start,aim,mid)#先把n-1个从起点搬到中间位置（mid作为终点参数，aim过渡）
        print('{}:{}->{}'.format(n,start,aim))#再把第n大的搬到终点
        count+=1
        hanoi(n-1,mid,start,aim)#再把n-1个从中间位置（mid作为起点参数）搬到终点
hanoi(3,'A','B','C')
print(count)