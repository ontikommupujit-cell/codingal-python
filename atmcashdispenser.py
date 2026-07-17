#the program for the atm cash dispenser
print('-------------------------------------------------------------------')
print('                     The ATM Cash Dispenser')
print('          Dispensing cash for customers one at a time')
print('-------------------------------------------------------------------')
print("")
notes=[100,50,20,5,1]
customers_served=0
total_dispensed=0
log=[]
serving=True
while serving:
    name=input('enter the. customer name')
    amount=int(input(f'hello{name} enter withdrawal ammount'))
    if amount <=0:
        print('invaild amount please enter a postive amount')
        continue
    print('dispensing{amount}units for {name}')
    print('-'*30)
    remaining=amount
    i=0
    used={}
    while i <len(notes):
        count=remaining//notes[i]
        if count>0:
            print(f'{count}X{notes[i]}-unit note(s)={count*notes[i]}')
            used[notes[i]]=count
            remaining -=count*notes[i]
        i+=1
    customers_served+=1
    total_dispensed+=amount
    log.append({'name':name,'used':used})
    print(f'transaction completed please collect your cash,{name}')
    again=input('next customer, yes or no').strip().lower()
    if again!="yes":
        serving=False
print('daily denomination report')
for note in notes:
    total_notes=0
    for entry in log :
        total_notes+=entry['used'].get(note,0)
    if total_notes >0:
        print(f"{note}-unit note dispense today{total_notes}")
print(f'customer-served-{customers_served}')
print(f"total dispensed-{total_dispensed}units")
print('atm session closed goodbye')
    
