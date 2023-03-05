sum=0
count=0
x=eval(input("Enter a number (negative to quit)>>"))
while x>=0:
    sum=sum+x
    count=count+1
    x=eval(input("Enter a number (negative to quit)>>"))
print ("\nThe average of the number is",sum/count)

