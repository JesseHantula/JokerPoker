from entities.models import Deck

class Poker:
    def __init__(self, scores):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = self.deck.deal()
        self.bot1_hand = self.deck.deal()
        self.bot2_hand = self.deck.deal()
        self.bot3_hand = self.deck.deal()

        self.scores = scores
        self.cards_to_replace = []

    def replace_cards(self, cards_to_replace):
        for card in cards_to_replace:
            self.player_hand.remove(card)
            self.player_hand.append(self.deck.draw())

    def check_hand(self, hand):
        pass
