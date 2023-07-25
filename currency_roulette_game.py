import requests
import random


def play(difficulty):
    user_guess = get_guess_from_user()
    money_interval = get_money_interval(difficulty, user_guess)
    converted_user_value = user_guess / money_interval[2]
    print(f'Your guess value is between the range {money_interval[0]} to {money_interval[1]} $.')
    if money_interval[0] <= converted_user_value <= money_interval[1]:
        print('Congratulations! Your guess is within the correct range.')
        return difficulty
    else:
        print('Oops! Your guess is outside the correct range.')



def get_money_interval(difficulty, user_guess):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    rate = data["rates"]["ILS"]
    lower_bound = user_guess - (5 - difficulty)
    upper_bound = user_guess + (5 - difficulty)
    return lower_bound / rate, upper_bound / rate, rate


def get_guess_from_user():
    random_value = random.randint(1, 100)
    return float(input(f'Enter your guess for ILS value to amount of {random_value} $: '))
