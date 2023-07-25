import random


def play(difficulty):
    print(f'welcome to the Guess Game!!')
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guess)

    if result is True:
        print('Congratulations!, You guessed the correct number')
        return difficulty
    else:
        print('The number you guessed is wrong !! Please try again !')


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    limit_num = difficulty
    while True:
        try:
            guess = int(input(f'Please choose a number between 1 - {limit_num}:'))
            if 1 <= guess <= limit_num:
                return guess
            else:
                print('Invalid input. Please enter a number within the specified range.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def compare_results(secret_number, guess_num):
    if secret_number == guess_num:
        return True
    else:
        return False
