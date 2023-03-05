def reverse(s):
    if s=="":
        return s
    else:
        return reverse (s[1:])+s[0]
#s=eval(input("Enter a number:"))
s='number'
print (reverse(s))
