try:
    number=(int(input("Enter a number")))
    print("the number is" , number)
except ValueError as ex:
    print("exepction",ex)
