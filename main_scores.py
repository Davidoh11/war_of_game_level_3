from flask import Flask

app = Flask(__name__)

SCORES_FILE_NAME = "scores.txt"


def read_score():
    """Reads the score from the scores file."""
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


@app.route('/')
def score_server():
    """Serves the score as an HTML response."""
    score = read_score()
    if score is not None:
        html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        html = """
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">ERROR</div></h1>
        </body>
        </html>
        """

    return html

