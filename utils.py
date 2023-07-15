import os

# 1. SCORES_FILE_NAME - A string representing a file name. By default "Scores.txt"
SCORES_FILE_NAME = "scores.txt"

# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
BAD_RETURN_CODE = -1

# 3. Screen_cleaner - A function to clear the screen (useful when playing memory game or before a new game starts).
def screen_cleaner():
    """Clears the console screen."""
    # Check the operating system and use the appropriate command
    if os.name == 'posix':  # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        # Unsupported operating system, print a newline character instead
        print('\n' * 100)
