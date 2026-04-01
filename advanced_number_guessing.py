import random

best = 3
play = True
while play:
    try:
        x = int(input('Enter the lowest number you like: '))
        y = int(input('Enter the highest number you like: '))
        if x > y:
            print("The highest number can't be lower than the lowest number")
            continue
        if x == y:
            print("The numbers can't be same")
            continue
        answer = random.randint(x, y)
        attempts = 0


        while True:

            attempts += 1
            guess = int(input(f'Guess the number between {x} and {y}: '))
            if attempts == 3:
                guess_stage = False
                print(f'You lose! The answer was {answer}, the best score is {best}')
                break
            elif guess > answer:
                print(f'Too high! You guessed {attempts} times')
                continue
            elif guess < answer:
                print(f'Too low! You guessed {attempts} times')
                continue
            else:
                print(f'Correct! You guessed {attempts} times')
                if attempts < best:
                    best = attempts
                    print(f'The best score is {best}')
                break
        while True:
            again = input('Do you want to play again? (y/n): ').lower()
            if again == 'n':
                play = False
                print(f'Thank you for playing! ')
                break
            elif again == 'y':
                break
            else:
                print('Please enter y or n')


    except ValueError:
        print('That is not a valid number. Try again.')
