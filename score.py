SCORES_FILE_NAME = "scores.txt"
POINTS_OF_WINNING = 0


def add_score(difficulty):
    """Adds the score to the current accumulated score in the scores file."""
    global POINTS_OF_WINNING

    # Calculate the points for winning based on the difficulty
    points = (difficulty * 3) + 5

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read())
            current_score += points
    except FileNotFoundError:
        # If the scores file does not exist, create a new one
        current_score = points

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))

    return current_score
