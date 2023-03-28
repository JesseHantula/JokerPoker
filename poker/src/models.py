import pygame
import random
from enum import Enum

class Suit(Enum):
    clubs = 0
    diamonds = 1
    hearts = 2
    spades = 3

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suit:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        return self.cards.pop()
    
    def length(self):
        return len(self.cards)
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 250
        
    def draw(self, deck):
        self.hand.append(deck.draw())
        
    def showHand(self):
        for card in self.hand:
            print(card.suit, card.value)
            
    def discard(self, index):
        self.hand.pop(index)
        
    def discardAll(self):
        self.hand = []

class Bot:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 250
        
    def draw(self, deck):
        self.hand.append(deck.draw())
        
    def showHand(self):
        for card in self.hand:
            print(card.suit, card.value)
            
    def discard(self, index):
        self.hand.pop(index)
        
    def discardAll(self):
        self.hand = []






