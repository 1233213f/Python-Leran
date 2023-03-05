amount=[1000.00,2311.00,3245.00,452.44]
rate=0.05
i=0
while i<len(amount):
    amount[i]=amount[i]*(rate+1)
    print (amount[i])
    i=i+1
