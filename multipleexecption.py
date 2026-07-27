try:
    num1,num2=eval(input("enter a number"))
    result=num1/num2
    print("the result is", result)
except ZeroDivisionError:
    print('division by zero is a error')
except SyntaxError:
    print('enter number sepreated by comma')
except:
    print("wrong input")
else:
    print('no exception')
finally:
    print('this will execute no matter what')
    