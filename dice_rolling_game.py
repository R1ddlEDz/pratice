import random


times = 0
while True:
    default = 0
    roll = input('roll the dice? (y/n): ').lower()


    if roll == 'y':
        user_input = int(input('How many dice do you want to roll? (1-6): '))
        if user_input >= 7 or user_input <= 0:
            print('invalid input')
        else:
            default += user_input
            dice_results = [random.randint(1, 6) for _ in range(default)]
            times += 1
            print("You rolled:", dice_results)
            print(f'You have rolled {times} times')

    elif roll == 'n':
        answer = 'thanks for playing!'
        print(answer)
        break
    else:
        print('invalid input')
