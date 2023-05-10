import pygame

class SetCards:
    """Class that represents the card images.
    Attributes:
        scale (int): scale of the card images
        card_size (tuple): size of the card images
        cards (dict): dictionary of the card images
        card_deck (Deck): deck of cards
    """
    def __init__(self, scale, card_size, card_deck, cards):
        """Constructor class that initializes the card images.
        Args:
            scale (int): scale of the card images
            card_size (tuple): size of the card images
            card_deck (Deck): deck of cards
            cards (dict): dictionary of the card images
        """
        self.scale = scale
        self.card_size = card_size
        self.cards = cards
        self.card_deck = card_deck 
        self.scaled_width = int(self.card_size[0] * self.scale)
        self.scaled_height = int(self.card_size[1] * self.scale)

    def set_cards(self):     
        """Sets the card images.
        """
        for card in self.card_deck.cards:
            self.cards[str(card)] = pygame.transform.scale(card.image, (self.scaled_width, self.scaled_height))

    def set_card_back(self, card_back):
        """Sets the card back image.
        Args:
            card_back (pygame.Surface): card back image
        Returns:
            card_back (pygame.Surface): scaled card back image
        """
        self.card_back = pygame.transform.scale(card_back, (self.scaled_width, self.scaled_height))
        return self.card_back
        