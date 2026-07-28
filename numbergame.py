import random
playing = True
number=str(random.randint(0,9))
print('I will think of a number between 0 to 9 and you have to guess the number 1 digit at a time')
print('when the game ends when you get 1 hero')
while playing:
    guess=(input('give me your number'))
    if number==guess:
        print('you win')
        print('the number was',number)
        break
    else:
        print('you are not right, keep guessing again')
