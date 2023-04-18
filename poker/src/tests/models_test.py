import unittest
from models import *

class TestCard(unittest.TestCase):
    def test_card(self):
        card = Card(Suit.SPADE, 1)
        self.assertEqual(card.suit, Suit.SPADE)
        self.assertEqual(card.value, 1)
        

class TestDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(deck.length(), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertEqual(deck.length(), 52)

    def test_deck_draw(self):
        deck = Deck()
        deck.shuffle()
        card = deck.draw()
        self.assertEqual(deck.length(), 51)

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player("test", 100)
        self.assertEqual(player.name, "test")
        self.assertEqual(player.money, 100)
        self.assertEqual(player.folded, False)

    def test_player_draw(self):
        deck = Deck()
        deck.shuffle()
        player = Player("test", 100)
        player.draw(deck)
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(deck.length(), 50)






