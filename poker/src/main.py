import pygame
from models import *
from engine import *

height = 720
width = 1280

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
        self.cardSize = (width * 0.1, height * 0.2)
        self.cards = {}
        self.cardBack = pygame.image.load("src/images/cards/BACK.png").convert_alpha()
        self.cardBack = pygame.transform.scale(self.cardBack, (int(self.cardSize[0] * self.scale), int(self.cardSize[1] * self.scale)))
        self.background = pygame.image.load("src/images/background.jpg")
        self.background = pygame.transform.scale(self.background, (width, height))
        window.blit(self.background, (0, 0))

        pygame.display.flip()

        for card in self.deck.cards:
            self.cards[card] = pygame.transform.scale(card.image, (int(self.cardSize[0] * self.scale), int(self.cardSize[1] * self.scale)))

        self.start_up_init()

    def start_up_init(self):
        self.poker = Poker()

        self.font1 = pygame.font.SysFont("oldwest", 100)
        self.font2 = pygame.font.SysFont("comicsans", 50)
        
        self.startText = self.font1.render("Texas Hold 'Em", 1, black)
        self.startTextLoc = (width/2 - self.startText.get_width()/2, height/2 - self.startText.get_height()/2 - 100)
        self.startButton = self.font2.render("Start", 1, red)
        self.startButtonLoc = (width/2 - self.startButton.get_width()/2, height/2 - self.startButton.get_height()/2)
        self.button = pygame.Rect(self.startButtonLoc[0], self.startButtonLoc[1], self.startButton.get_width(), self.startButton.get_height())

        self.state = 0

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.state = 1

        window.blit(self.startText, self.startTextLoc)
        window.blit(self.startButton, self.startButtonLoc)

        pygame.display.update()

    def main(self):
        if self.state == 0:
            self.start()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
            self.results()
        elif self.state == 3:
            self.end()


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption("POKER")
    Run = Game()
    while True:
        Run.main()
    