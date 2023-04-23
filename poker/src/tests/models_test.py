import unittest
from entities.models import Deck, Card, Suit


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

    def test_deck_deal(self):
        deck = Deck()
        deck.shuffle()
        hand = deck.deal()
        self.assertEqual(deck.length(), 47)
        self.assertEqual(len(hand), 5)
        
