book_list=["diary of a wimpy kid","percy jackson","holes","the hobbit","coraline"]
copies=[5,2,0,4,3]
library={name:amount for name,amount in zip(book_list,copies)}
print("Library:",library)
available=[name for name in book_list if library[name]>0]
print("Available Books:",available)
choice=input("Enter a book to borrow: ")
if choice not in library or library[choice]==0:
    print("Sorry,",choice,"is unavailable.")
    exit()
fees=[3,6,5,4,7]
extra=int(input("Extra fee: "))
new_fees=list(map(lambda x:x+extra,fees))
print("Updated Fees:",new_fees)
index=book_list.index(choice)
fee=new_fees[index]
print("Fee for",choice,":",fee)
library[choice]-=1
print(choice,"has been borrowed.")
print()
print("===== LIBRARY SUMMARY =====")
print("Borrowed Book:",choice)
print("Late Fee:",fee)
print("Library Stock:",library)
print("===========================")