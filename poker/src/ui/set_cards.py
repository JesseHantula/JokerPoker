import pygame

class SetCards:
    def __init__(self, scale, card_size, card_deck, cards):
        self.scale = scale
        self.card_size = card_size
        self.cards = cards
        self.card_deck = card_deck 
        self.scaled_width = int(self.card_size[0] * self.scale)
        self.scaled_height = int(self.card_size[1] * self.scale)

    def set_cards(self):     
        for card in self.card_deck.cards:
            self.cards[str(card)] = pygame.transform.scale(card.image, (self.scaled_width, self.scaled_height))

    def set_card_back(self, card_back):
        self.card_back = pygame.transform.scale(card_back, (self.scaled_width, self.scaled_height))
        return self.card_back
        