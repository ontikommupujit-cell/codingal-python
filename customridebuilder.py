print("=====================================")
print('   welcome to the ride builder ')
print("=====================================")
print('Step 1: Pick Your Vehicle')
print('1=car ')
print('2=bike')
print('3=train')
print("=========================================")
choice= (int(input('enter your choice')))
print('you have chosen option',choice)
print("=========================================")
print()
if choice==1:
    print('step 2: Pick your Car type')
    print('1=sedan')
    print('2=suv')
    car_type=(int (input('enter your choice')))
    print()
    if car_type==1:
        print('you have chosen a sedan')
        print('top speed is 80km/h')
        print('best for family trips')
    else:
        print('you have chosen a suv')
        print('top speed is 100km/hr')
        print('best for off road trips')
elif(choice==2):
    print("step 2:choose your bike")
    print("1=scooty")
    print('2=mountain bike')
    print()
    bike_type=(int(input('enter your choice')))
    print()
    if bike_type==1:
        print('you have chosen a scooty')
        print('top speed is 50km/hr')
        print('best for city roads')
    else:
        print('you have chosen a mountain bike')
        print("the top speed is 80km/hr")
        print('best for off road trips')
elif (choice==3):
    print('step 2:choose your train')
    print('1=express')
    print('2=local')
    train_type=(int(input('enter your choice')))
    print()
    if train_type==1:
        print('you have chosen an express train')
        print('top speed is 150km/hr')
        print('best for long distance travel')
    else:
        print('you have chosen a local train')
        print('the top speed is 80 km/hr')
        print('best for short travel')
else:
    print('invalid choice')
    print()
print('==========================================')
print(       "Your custom ride is ready")
print('==========================================')



      

