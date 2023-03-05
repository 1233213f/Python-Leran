from math import*
a=eval(input("Please enter a set of numbers:"))
b=str(a)
max=b[0]
for i in range (1,len(b)):
    x=b[i]
    if x>max:
        max=x
print ("The largest value is",max)
