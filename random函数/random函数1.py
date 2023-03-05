
from random import*
from math import*
list=[1,2,3,4,5,6,7]

a,b,c,k,x=eval(input("Do enter the coeficients a,b,c,k,x:"))
print("给随机一个种子值",seed(x))
print("生成一个a到b之间的随机小数",uniform(a,b))
print("生成一个a到b之间的随机整数",randint(a,b))
print("随机生成一个a到b以c递增的一个元素",randrange(a,b,c))
print("随机从列表中返回一个元素",choice(list))
print("将列表中元数打乱",shuffle(list))
print("从指定列表中随机获取k个元素",sample(list,k))
