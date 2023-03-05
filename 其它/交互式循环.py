def main():
    sum=0
    count=0
    mo="yes"
    while mo[0]=="y"or mo[0]=="Y":
        x=eval(input("Enter a number (negative to quit)>>"))
        sum=sum+x
        count=count+1
        mo=input("Do you have more numbers(yes or no)?")
    print ("\nThe average of the number is",sum/count)
main()
