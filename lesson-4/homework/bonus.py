import random
choices=['s', 'p', 'r']
user_point=0
computer_point=0
while user_point<5 and  computer_point<5:
    user_choice=input('Enter one of them(scinsors, rock, paper, or scissors): ').lower()
    if user_choice not in choices:
        print("invalied choices. Please enter valid choice(s, r, or p)")
        continue
    computer_choice=random.choice(choices)

    print(f'you - {user_choice} computer -{computer_choice}')

    if user_choice==computer_choice:
        print('it is a tie')
    elif(user_choice=='s' and computer_choice=='p') or\
        (user_choice=='r' and computer_choice=='s') or \
        (user_choice=='p' and computer_choice=='r'):
        user_point+=1 
        print('You won this game')
        
    else:
        computer_point+=1
        print('computer won this game')
        

    

if computer_point>user_point:
        print('computer won ')
elif computer_point<user_point:
             print('you won ')
else:
        print('it is a tie game')         