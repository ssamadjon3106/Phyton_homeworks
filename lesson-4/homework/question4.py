import random

while True:
    count = 0
    answer = 0
    num = random.randint(1, 100)

    while answer != num and count < 10:
        answer = int(input("Enter a number between 1 and 100: "))
        if answer > num:
            print('Too high.')
            count += 1
        elif answer < num:
            print('Too low.')
            count += 1
        else:
            print('🎉 You guessed it right!', count + 1, 'attempts')
            break

    if answer == num:
        break  # Exit after winning

    if count == 10:
        print('You lost.')
        choice = input('Want to play again? (yes / no): ').lower()
        if choice in ['y', 'yes', 'ok']:
            continue  # Start game again
        else:
            print('Thank you for participating!')
            break  # Exit the game
