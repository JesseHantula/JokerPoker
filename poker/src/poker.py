from enum import Enum
import pygame
from models import *

class GameState(Enum):
    PLAYING = 1
    WON = 2
    LOST = 3

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player()
        self.player2 = Bot()
        self.player3 = Bot()
        self.player4 = Bot()
        self.state = GameState.PLAYING