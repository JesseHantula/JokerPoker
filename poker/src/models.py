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
        self.image = pygame.image.load("src/images/cards/" + self.suit.name \
                                       + "-" + str(self.value) + ".svg")

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

class Player:
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money
        self.folded = False
        self.raise_key = False
        self.call_key = False
        self.fold_key = False

    def draw(self, deck):
        for _ in range(2):
            self.hand.append(deck.draw())

    def make_bet(self, amount):
        self.money -= amount

    def fold(self):
        self.hand = []

    def discard_all(self):
        self.hand = []

class Round:
    def __init__(self):
        self.pot = 0
        self.current_bet = 0
        self.community_cards = []
        self.players = []

    def get_community_cards(self, deck):
        for _ in range(3):
            self.community_cards.append(deck.draw())

    def add_community_card(self, deck):
        self.community_cards.append(deck.draw())

    def update_pot(self, amount):
        self.pot += amount

    def update_bet(self, amount):
        self.current_bet = amount
