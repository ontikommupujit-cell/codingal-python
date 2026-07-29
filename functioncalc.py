def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('You cant divide with zero')
def main():
    print('Welcome to the Calculator')
    print("press 1 for addition")
    print('press 2 for subtraction')
    print('press 3 for multiplacation')
    print('press 4 for division')
    user_choice=(int(input("enter a number")))
    if user_choice!=1:
        print('invalid choose another number')
    if user_choice!=2:
            print('invalid choose another number')
    if user_choice!=3:
            print('invalid choose another number')
    if user_choice!=4:
            print('invalid choose another number')
    if user_choice==1:
         result=add(num1,num2)
    elif user_choice==2:
            result=subtract(num1,num2)
    elif user_choice==3:
            result=multiply(num1,num2)
    elif user_choice==4:
            result=divide(num1,num2)
    try:
        num1=float(input('enter a number'))
        num2=float(input('enter a number'))
    except ValueError:
        print('invalid number, enter a different one')
    



  




