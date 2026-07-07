amount=int(input("Enter the amount withdrawal: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("the 100 rupees notes are ",note1)
print("the 50 rupees notes are",note2)
print("the 10 rupees notes are",note3)
