
from termgamelib.factory import GameFactory
import flask

app = flask.Flask(__name__)


def play_hangman():
    """Route-driven function that preselects the hangman game from the library.

    Some docstring on how this function works, what algorithms it uses and how
    it interacts with the rest of the program.

    Args:
        None
    
    RETURNS:
        "something" string to have an output
    
    """
    GameFactory.select_game("hangman")
    return "something"


@app.route('/')
def home():
    return play_hangman()

if __name__=='__main__':
    app.run(debug=False)

