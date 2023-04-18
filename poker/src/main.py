"""
this module is the main module of the game
"""
import sys
import pygame
from models import Deck
from engine import Poker


HEIGHT = 720
WIDTH = 1280

#global colors that are used
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.scale = 0.4
        self.card_size = (WIDTH * 0.1, HEIGHT * 0.2)
        self.cards = {}
        self.card_back = pygame.image.load("src/images/cards/BACK.png").convert_alpha()
        scaled_width = int(self.scale * self.card_size[0])
        scaled_height = int(self.scale * self.card_size[1])
        self.card_back = pygame.transform.scale(self.card_back, (scaled_width, scaled_height))
        self.background = pygame.image.load("src/images/background.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        window.blit(self.background, (0, 0))

        pygame.display.flip()

        for card in self.deck.cards:
            self.cards[card] = pygame.transform.scale(card.image, scaled_width, scaled_height)

        self.start_up_init()

    def start_up_init(self):
        self.poker = Poker()

        self.font1 = pygame.font.SysFont("oldwest", 100)
        self.font2 = pygame.font.SysFont("comicsans", 50)
        self.start_text = self.font1.render("Texas Hold 'Em", 1, black)
        self.start_text_loc = (WIDTH/2 - self.start_text.get_width()/2, \
                             HEIGHT/2 - self.start_text.get_height()/2 - 100)
        self.start_button = self.font2.render("Start", 1, red)
        self.start_button_loc = (WIDTH/2 - self.start_button.get_width()/2, \
                               HEIGHT/2 - self.start_button.get_height()/2)
        self.button = pygame.Rect(self.start_button_loc[0], self.start_button_loc[1], \
                                  self.start_button.get_width(), self.start_button.get_height())

        self.state = 0

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.state += 1

        window.blit(self.start_text, self.start_text_loc)
        window.blit(self.start_button, self.start_button_loc)

        pygame.display.update()

    def main(self):
        if self.state == 0:
            self.start()
        elif self.state == 1:
            self.play()

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption("POKER")
    Run = Game()
    while True:
        Run.main()
    