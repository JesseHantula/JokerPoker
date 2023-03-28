import unittest
from models import *

class TestCard(unittest.TestCase):
    def test_card(self):
        card = Card(1, 1)
        self.assertEqual(card.suit, 1)
        self.assertEqual(card.value, 1)
        

class TestDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(deck.length(), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertEqual(deck.length(), 52)




