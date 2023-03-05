def addInterest(balance,rate):
    newBalance=balance * (1+rate)
    return newBalance
def main():
    amount=1000.00
    rate=0.05
    t=addInterest(amount, rate)
    print(t)
main()
