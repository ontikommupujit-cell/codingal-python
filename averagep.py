a=(int(input('enter a number')))
b=(int(input('enter a number')))
c=(int(input('enter a number')))
average=a+b+c/3
print(average)
if average>a and average>b and average>c:
    print('average is greater than a b and c')
elif average>a and average>b:
    print('average is greater than a and b')
elif average>a and average>c:
    print('average is greater than a and c')
elif average>a:
    print('average is greater than a')
elif average>b: 
    print('average is greater than b')
elif average>c:
    print('average is greater than c')
