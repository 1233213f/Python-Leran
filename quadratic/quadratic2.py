import math
def main():
    print("Let us finds the solutions to aa quadratic.\n")
    try:
        a,b,c=eval(input("Do enter the coeficients (a,b,c):"))
        discRoot=math.sqrt(b*b-4*a*c)
        root1= (-b+discRoot)/(2*a)
        root2= (-b-discRoot)/(2*a)
        print("\nThe solutions are:",root1, root2)
    except ValueError as excObj:
        if str(excObj)=="math domain error":
            print("No Real Roots.")
        else:
                print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print ("/nYour input were not all numbers.")
    except SyntaxError:
        print ("\nYour input was not in the correct from. Missing comma?")
    except :
        print("\nSomething went wrong, sorry!")
main()
