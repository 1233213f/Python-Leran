import math
def main():
    print("Let us finds the solutions to aa quadratic\n")
    a,b,c=eval(input("Do enter the coeficients a,b,c:"))
    delta=b*b-4*a*c
    if delta<0:
        print ("\nThe eauation has no real roots!")
    elif delta==o:
        x=-b/(2*a)
        print ("\nThere is a double root at",x)
    else:
        discRoot = math.sqrt(b*b-4*a*c)
        root1= (-b+discRoot)/(2*a)
        root2= (-b-discRoot)/(2*a)
        print("\nThe solutions are:",root1, root2)
main()
