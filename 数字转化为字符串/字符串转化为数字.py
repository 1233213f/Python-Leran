from math import*
numbers = ['1', '5', '10', '8']
#numbers = list(map(int, numbers))
#print (numbers)
#numbers = [ int(x) for x in numbers ]
#print (numbers)
#numbers = map(int, numbers)
#print (numbers)
for i, v in enumerate(numbers):
    numbers[i] = int(v)
print (numbers)
