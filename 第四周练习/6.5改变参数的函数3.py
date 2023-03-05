def addInterest(balance,rate):
#    for i in range (len(balance)):
#        balance[i]=balance[i]*(1+rate)
    i=0
    while i<len(balance):
        balance[i]=balance[i]*(1+rate)
        i=i+1
def test():
    amount=[1000.00,105.00,3500,739]
    rate=0.05
    addInterest (amount ,rate)
    print(amount)
    print (addInterest(amount,rate))
test()
