from guess_game import play as guess_game
from memory_game import play as memory_game
from currency_roulette_game import play as currency_roulette_game
from score import add_score


def welcome(name):
    blue = '\033[94m'
    formatted_name = blue + name
    line_1 = f'{formatted_name} Welcome to the World of Games (WOG)'
    line_2 = f'Here you can find many cool games to play'
    return line_1 + '\n' + '\n' + line_2


def load_game():
    try:
        game_options = int(input('Please choose a game to play: '
                                 + '\n'
                                 + '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'
                                 + '\n'
                                 + '2. Guess Game - guess a number and see if you chose like the computer '
                                 + '\n'
                                 + '3. Currency Roulette - try and guess the value of a random amount of USD in ILS '
                                 + '\n' + 'Enter your choose :'))

        if game_options < 0 or game_options > 3:
            print('Invalid Game number, please choose game option from 1 - 3')
            print()
            return load_game()
        difficulty = int(input('Please choose game difficulty level from 1 - 5: '))

        if difficulty < 1 or difficulty > 5:
            print('Difficulty is out of range')
            return load_game()
        if game_options == 1:
            if memory_game(difficulty):
                add_score(difficulty)

        elif game_options == 2:
            if guess_game(difficulty):  # Check if user won the game
                add_score(difficulty)
        elif game_options == 3:
            if currency_roulette_game(difficulty):
                add_score(difficulty)
    except ValueError:
        print('Invalid input. Please enter a valid integer for game options.')
        print()
        return load_game()


