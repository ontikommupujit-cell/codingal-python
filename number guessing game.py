import random
secret_number=random.randint(1,50)
attempts=5
print('Guess the number between 1 and 50')
while attempts>0:
    guessed_number=(print(int(input('enter a number'))))
    if guessed_number==secret_number:
        print('game over')
    attempts-=1
if secret_number>=40:
    print('hot')
elif secret_number>=30:
    print('warm')
elif secret_number>=20:
    print('cold')
elif secret_number>=10:
    print('ice cold')

    

