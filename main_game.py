from live import welcome, load_game
from main_scores import app

name = 'Please enter your user name for this game: '
green = '\033[92m'
formatted_name = green + name
name = str(input(formatted_name))

print(welcome(name))
load_game()

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)

