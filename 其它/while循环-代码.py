sum=0
number=0
n=eval(input("Please enter a number:"))
while number<n:
    number+=1
    sum+=number
    if sum>100:
        break
print ("The number is ",number)
print ("The sum is ",sum)
