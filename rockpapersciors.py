import random
while True:
    user_action=input('enter a choice, rock paper or scissors')
    possible_action=["rock",'paper','scissors']
    computer_action=random.choice(possible_action)
    print(f'you choose{user_action},computer_chose{computer_action}')
    if user_action == computer_action:
        print(f'both of you selected{user_action}this is a tie')
    elif user_action=="rock":
        if computer_action=="scissors":
            print('rock smashes scissors the user wins')
        else:
            print('paper covers rock you loose') 
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock you win")
        else:
            print('scissors cut paper and you loose')
    elif user_action=="scissor":
        if computer_action=="paper":
            print('scissor cut paper you win')
        else:
            print('rock smashes scissor you loose')