import unittest
from entities.models import Deck, Card, Suit
from entities.engine import Poker

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
        
class TestPoker(unittest.TestCase):
    def test_poker(self):
        poker = Poker([0,0,0,0])
        self.assertEqual(len(poker.player_hand), 5)
        self.assertEqual(len(poker.bot1_hand), 5)
        self.assertEqual(len(poker.bot2_hand), 5)
        self.assertEqual(len(poker.bot3_hand), 5)

    def test_poker_check_hand(self):
        poker = Poker([0,0,0,0])

        royal_flush = [Card(Suit.SPADE, 1), Card(Suit.SPADE, 10), Card(Suit.SPADE, 11), Card(Suit.SPADE, 12), Card(Suit.SPADE, 13)]
        self.assertEqual(poker.check_hand(royal_flush), 9)

        straight_flush = [Card(Suit.SPADE, 9), Card(Suit.SPADE, 8), Card(Suit.SPADE, 7), Card(Suit.SPADE, 6), Card(Suit.SPADE, 5)]
        self.assertEqual(poker.check_hand(straight_flush), 8)

        four_of_a_kind = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 1), Card(Suit.SPADE, 2)]
        self.assertEqual(poker.check_hand(four_of_a_kind), 7)

        full_house = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 2)]
        self.assertEqual(poker.check_hand(full_house), 6)

        flush = [Card(Suit.SPADE, 1), Card(Suit.SPADE, 5), Card(Suit.SPADE, 8), Card(Suit.SPADE, 3), Card(Suit.SPADE, 10)]
        self.assertEqual(poker.check_hand(flush), 5)

        straight = [Card(Suit.SPADE, 9), Card(Suit.HEART, 8), Card(Suit.CLUB, 7), Card(Suit.DIAMOND, 6), Card(Suit.SPADE, 5)]
        self.assertEqual(poker.check_hand(straight), 4)
        
        three_of_a_kind = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(poker.check_hand(three_of_a_kind), 3)

        two_pair = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(poker.check_hand(two_pair), 2)

        one_pair = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 3), Card(Suit.SPADE, 4)]
        self.assertEqual(poker.check_hand(one_pair), 1)

        high_card = [Card(Suit.SPADE, 1), Card(Suit.HEART, 2), Card(Suit.CLUB, 3), Card(Suit.DIAMOND, 4), Card(Suit.SPADE, 6)]
        self.assertEqual(poker.check_hand(high_card), 0)