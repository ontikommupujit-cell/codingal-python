def Greet_Customer():
    print('Welcome to my Lemonade Stand')
    print('You will find the best lemonadestand here')
Greet_Customer()
cups=(int(input('How many Cups')))
price=(float(input('How much was the price')))
def calculate_total_cost(price,cups):
    total_cost=(price*cups)
    return total_cost
total=calculate_total_cost(price,cups)
roundedtotal=round(total,2)
print('total_cost-',roundedtotal)
amount_paid=(float(input('Enter the amount paid by the customer')))
def calculate_change(amount_paid,total):
    change=amount_paid-total
    return change
change_due=calculate_change(amount_paid,roundedtotal)
roundedchange=round(change_due,2)
def thank_you_message(cups):
    if cups>=5:
        return 'big order thank you for your support' 
    else:
        return "thanks for stoping by"
closing_message=thank_you_message(cups)
print ('price per cup',price)
print('cups sold',cups)
print('total',roundedtotal)
print('amount paid',amount_paid)
print('change due',roundedchange)