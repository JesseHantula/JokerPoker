import pygame

height = 720
width = 1280

class Start:
    def __init__(self):
        self.scale = 0.4
        self.cardSize = (width * 0.1, height * 0.2)
        self.cards = {}
        self.cardBack = pygame.image.load("src/images/cards/BACK.png").convert_alpha()
        scaled_width = int(self.scale * self.cardSize[0])
        scaled_height = int(self.scale * self.cardSize[1])
        self.cardBack = pygame.transform.scale(self.cardBack, (scaled_width, scaled_height))
        self.background = pygame.image.load("src/images/background.jpg")
        self.background = pygame.transform.scale(self.background, (width, height))
        