import random
from enum import Enum
import pygame


class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load("src/images/cards/" + self.suit.name
                                       + "-" + str(self.value) + ".svg")

    def __str__(self):
        return f"{self.value} of {self.suit.name}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)

    def deal(self):
        hand = []
        for _ in range(5):
            hand.append(self.draw())
        return hand
