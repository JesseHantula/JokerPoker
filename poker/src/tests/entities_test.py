import unittest
from entities.models import Deck, Card, Suit
from entities.engine import Poker
import constants

class TestConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(constants.WIDTH, 1280)
        self.assertEqual(constants.HEIGHT, 720)
        self.assertEqual(constants.RED, (200, 0, 0))
        self.assertEqual(constants.BLACK, (0, 0, 0))
        self.assertEqual(constants.WHITE, (255, 255, 255))
        self.assertEqual(constants.GREEN, (0, 255, 0))
        self.assertEqual(constants.BLUE, (0, 0, 255))
        self.assertEqual(constants.FONT1, ("casino", 100))
        self.assertEqual(constants.FONT2, ("oldwest", 50))
        self.assertEqual(constants.FONT3, ("comic sans", 30))
        
class TestCard(unittest.TestCase):
    def test_card(self):
        card = Card(Suit.SPADE, 1)
        self.assertEqual(card.suit, Suit.SPADE)
        self.assertEqual(card.value, 1)

    def test_card_str(self):
        card = Card(Suit.SPADE, 1)
        self.assertEqual(str(card), "1 of SPADE")

    def test_card_eq(self):
        card1 = Card(Suit.SPADE, 1)
        card2 = Card(Suit.SPADE, 1)
        self.assertEqual(card1, card2)

class TestDeck(unittest.TestCase):
    def test_deck_length(self):
        deck = Deck()
        self.assertEqual(deck.length(), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        deck2 = Deck()
        deck.shuffle()
        self.assertNotEqual(deck, deck2)

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
        self.assertEqual(int(poker.check_hand(royal_flush)), 9)

        straight_flush = [Card(Suit.SPADE, 9), Card(Suit.SPADE, 8), Card(Suit.SPADE, 7), Card(Suit.SPADE, 6), Card(Suit.SPADE, 5)]
        self.assertEqual(int(poker.check_hand(straight_flush)), 8)

        four_of_a_kind = [Card(Suit.SPADE, 6), Card(Suit.HEART, 6), Card(Suit.CLUB, 6), Card(Suit.DIAMOND, 6), Card(Suit.SPADE, 2)]
        self.assertEqual(int(poker.check_hand(four_of_a_kind)), 7)

        full_house = [Card(Suit.SPADE, 5), Card(Suit.HEART, 5), Card(Suit.CLUB, 5), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 2)]
        self.assertEqual(int(poker.check_hand(full_house)), 6)

        flush = [Card(Suit.SPADE, 4), Card(Suit.SPADE, 5), Card(Suit.SPADE, 8), Card(Suit.SPADE, 3), Card(Suit.SPADE, 10)]
        self.assertEqual(int(poker.check_hand(flush)), 5)

        straight = [Card(Suit.SPADE, 9), Card(Suit.HEART, 8), Card(Suit.CLUB, 7), Card(Suit.DIAMOND, 6), Card(Suit.SPADE, 5)]
        self.assertEqual(int(poker.check_hand(straight)), 4)
        
        three_of_a_kind = [Card(Suit.SPADE, 8), Card(Suit.HEART, 8), Card(Suit.CLUB, 8), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(int(poker.check_hand(three_of_a_kind)), 3)

        two_pair = [Card(Suit.SPADE, 6), Card(Suit.HEART, 6), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(int(poker.check_hand(two_pair)), 2)

        two_pair_2 = [Card(Suit.SPADE, 1), Card(Suit.HEART, 2), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 3), Card(Suit.SPADE, 3)]
        self.assertEqual(round(poker.check_hand(two_pair_2), 2), 2.03)

        one_pair = [Card(Suit.SPADE, 10), Card(Suit.HEART, 10), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 3), Card(Suit.SPADE, 4)]
        self.assertEqual(int(poker.check_hand(one_pair)), 1)

        high_card = [Card(Suit.SPADE, 10), Card(Suit.HEART, 2), Card(Suit.CLUB, 3), Card(Suit.DIAMOND, 4), Card(Suit.SPADE, 6)]
        self.assertEqual(int(poker.check_hand(high_card)), 0)

    def test_poker_check_hand_with_ace(self):
        poker = Poker([0,0,0,0])

        four_of_a_kind = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 1), Card(Suit.SPADE, 2)]
        self.assertEqual(round(poker.check_hand(four_of_a_kind), 2), 7.14)

        full_house = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 2)]
        self.assertEqual(round(poker.check_hand(full_house), 2), 6.14)

        flush = [Card(Suit.SPADE, 1), Card(Suit.SPADE, 5), Card(Suit.SPADE, 8), Card(Suit.SPADE, 3), Card(Suit.SPADE, 10)]
        self.assertEqual(round(poker.check_hand(flush), 2), 5.14)

        straight = [Card(Suit.SPADE, 1), Card(Suit.HEART, 2), Card(Suit.CLUB, 3), Card(Suit.DIAMOND, 4), Card(Suit.SPADE, 5)]
        self.assertEqual(round(poker.check_hand(straight), 2), 4.14)

        three_of_a_kind = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 1), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(round(poker.check_hand(three_of_a_kind), 2), 3.14)

        two_pair = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 2), Card(Suit.SPADE, 3)]
        self.assertEqual(round(poker.check_hand(two_pair), 2), 2.14)

        one_pair = [Card(Suit.SPADE, 1), Card(Suit.HEART, 1), Card(Suit.CLUB, 2), Card(Suit.DIAMOND, 3), Card(Suit.SPADE, 4)]
        self.assertEqual(round(poker.check_hand(one_pair), 2), 1.14)

        high_card = [Card(Suit.SPADE, 1), Card(Suit.HEART, 2), Card(Suit.CLUB, 3), Card(Suit.DIAMOND, 4), Card(Suit.SPADE, 6)]
        self.assertEqual(round(poker.check_hand(high_card), 2), 0.14)
        
    def test_poker_replace_cards(self):
        poker = Poker([0,0,0,0])
        hand = poker.player_hand
        hand2 = poker.replace_cards(hand)
        self.assertNotEqual(hand, hand2)
        
    def test_poker_convert(self):
        poker = Poker([0,0,0,0])
        winner = (0, 9.14)
        self.assertEqual(poker.convert(winner), ["You", "Royal Flush"])
        winner = (0, 8.09)
        self.assertEqual(poker.convert(winner), ["You", "Straight Flush"])
        winner = (1, 7.14)
        self.assertEqual(poker.convert(winner), ["Bot 1", "Four of a Kind"])
        winner = (2, 6.14)
        self.assertEqual(poker.convert(winner), ["Bot 2", "Full House"])
        winner = (3, 5.14)
        self.assertEqual(poker.convert(winner), ["Bot 3", "Flush"])
        winner = (0, 4.14)
        self.assertEqual(poker.convert(winner), ["You", "Straight"])
        winner = (1, 3.14)
        self.assertEqual(poker.convert(winner), ["Bot 1", "Three of a Kind"])
        winner = (2, 2.14)
        self.assertEqual(poker.convert(winner), ["Bot 2", "Two Pair"])
        winner = (3, 1.14)
        self.assertEqual(poker.convert(winner), ["Bot 3", "Pair"])
        winner = (0, 0.14)
        self.assertEqual(poker.convert(winner), ["You", "High Card"])

    def test_poker_get_winner(self):
        poker = Poker([0,0,0,0])
        winner = poker.get_winner()
        self.assertEqual(len(winner), 2)
        self.assertTrue(winner[0] >= 0 and winner[0] <= 3)
        self.assertTrue(winner[1] >= 0 and winner[1] <= 9)
        


