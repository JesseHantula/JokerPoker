import random
from enum import Enum
import pygame


class Suit(Enum):
    """
    Class that enumerates the suits of a deck of cards.
    """
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Card:
    """
    Class that represents a card in a deck of cards.
    Attributes: suit (Suit): suit of the card
                value (int): value of the card
    """
    def __init__(self, suit, value):
        """
        Constructor class that initializes the card. It also loads the image of the card.
        Args: suit (Suit): suit of the card
              value (int): value of the card
        """
        self.suit = suit
        self.value = value
        self.image = pygame.image.load("src/images/cards/" + self.suit.name
                                       + "-" + str(self.value) + ".svg")

    def __str__(self):
        """
        Returns a string representation of the card.
        """
        return f"{self.value} of {self.suit.name}"

class Deck:
    """
    Class that represents a deck of cards.
    """
    def __init__(self):
        """
        Constructor class that initializes the deck of cards. Does this by adding cards with values 1-13 for each suit.
        """
        self.cards = []
        for suit in Suit:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Draws a card from the deck. Returns the card.
        """
        return self.cards.pop()

    def length(self):
        """
        Returns the length of the deck.
        """
        return len(self.cards)

    def deal(self):
        """
        Deals a hand of 5 cards from the deck. Returns the hand.
        """
        hand = []
        for _ in range(5):
            hand.append(self.draw())
        return hand
