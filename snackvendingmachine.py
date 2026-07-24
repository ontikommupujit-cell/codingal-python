def calculatechange(price,paid):
    change=paid-price
    return change
print("-----------------------------------------")
print(' Welcome to the Snack Vending Machince')
print('-----------------------------------------')
snackprice=100
print(f'the snack price is {snackprice}units')
print('the accepted cash is 1 dollar bill,5 dollar bill and a 10 dollar bill')
total_inserted=0
bill_inserted=0
while True:
    bill=int(input("insert a bill, only a 1 dollar,5 dollar and a 10 dollar bill shall be accepted"))
    if bill != 1 and bill !=5 and bill !=10:
        print('Not Accepted, Pls enter a valid bill')
        continue
    total_inserted+=bill
    bill_inserted+=1
    print(f"inserted{bill}total so far{total_inserted}")
    if total_inserted>=snackprice:
        print('Enough amount is received')
        break
changedue=calculatechange(total_inserted,snackprice)
print('dispensing your snack')
if changedue==0:
    pass
else:
    print(f'here is your change{changedue}units')
print('-------------------------')
print('   Purchase Summery')
print('snack price',snackprice)
print('bill inserted',bill_inserted)
print('total paid',total_inserted)
print('change given',changedue)
print('thank you for your purchase')
print('--------------------------')