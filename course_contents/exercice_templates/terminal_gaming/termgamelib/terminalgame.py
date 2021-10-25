
import abc

class TerminalGame(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def display(cls) -> None:
        """Abstract static method that is responsible for game board display"""

    @classmethod
    @abc.abstractmethod
    def play(cls) -> None:
        """ Abstract static method that allows for playing of the game"""