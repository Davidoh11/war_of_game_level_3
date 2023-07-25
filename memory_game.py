import random
import time
import os


def play(difficulty):
    print(f'welcome to the Memory Game!!')
    print(f'Memory Game is starting now!!')
    sequence_numbers = generate_sequence(difficulty)
    for num in sequence_numbers:
        print(num, end=' ', flush=True)  # Display the number
        time.sleep(0.7)   
        print('\r', end='', flush=True)  # Clear the number from the console
    print(' ' * 5)
    print('Memorize this sequence numbers now!')
    user_sequence = get_list_from_user(difficulty)
    print(f'Your sequence numbers', user_sequence)
    if is_list_equal(sequence_numbers, user_sequence) is True:
        print(f'Congratulations! you memorize all numbers!')
        return difficulty
    if is_list_equal(sequence_numbers, user_sequence) is False:
        print(f'Sorry! you did not memorize all numbers! sequence_numbers was {sequence_numbers}')


def generate_sequence(difficulty):
    sequence = []
    for x in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence


def get_list_from_user(difficulty):
    user_list = []
    for y in range(difficulty):
        num = int(input(f'Enter a {difficulty} number/s: '))
        user_list.append(num)
    return user_list


def is_list_equal(sequence_numbers, user_sequence):

    if sequence_numbers == user_sequence:
        return True
    else:
        return False
