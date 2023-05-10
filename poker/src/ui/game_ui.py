"""
This module is the main UI module of the game
"""
import sys
import pygame
from entities.models import Deck
from entities.engine import Poker
from ui.start_screen import StartScreen
from ui.game_screen import GameScreen
from ui.end_screen import EndScreen
from ui.button import Button
from ui.set_cards import SetCards
import constants

class Game:
    """
    Class that represents the game UI.
    """
    def __init__(self):
        """
        Constructor class that initializes the game. Initializes the window, the deck of cards, and the card images.
        """
        pygame.init()
        self.window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT), 0, 32)
        self.deck = Deck()
        self.scale = 0.75
        self.card_size = (constants.WIDTH * 0.1, constants.HEIGHT * 0.2)
        self.background = pygame.image.load("src/images/background.jpg")
        self.background = pygame.transform.scale(self.background, (constants.WIDTH, constants.HEIGHT))
        self.window.blit(self.background, (0, 0))
        self.cards = {}
        self.card_back = pygame.image.load("src/images/cards/BACK.png").convert_alpha()
        card_setter = SetCards(self.scale, self.card_size, self.deck, self.cards)
        card_setter.set_cards()
        self.card_back = card_setter.set_card_back(self.card_back)
        pygame.display.flip()

        self.start()

    def start(self):
        """
        Starts the game. 
        """
        self.state = 0
        self.scoreboard = [0, 0, 0, 0]
        self.poker = Poker(self.scoreboard)
        self.draw_start = StartScreen()
        self.start_button = Button(525, 350, 200, 100, constants.RED, "Start", (0, 0, 0), "oldwest", 50, True)
        self.draw_start.draw_screen(self.window, self.start_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.use():
                    self.state = 1
                    
    def play(self):
        """
        Function that runs the main game screen.
        """   
        self.draw_game = GameScreen()
        self.replace_button = Button(900, 80, 200, 100, constants.RED, "Replace", constants.BLACK, constants.FONT1[0], 50, True)
        self.draw_game.set_locs(self.card_size)
        card_locs = self.draw_game.get_locs()
        self.running = True
        #sets up a loop to make updating the screen easier
        while self.running:
            self.window.blit(self.background, (0, 0))
            self.draw_game.draw_screen(self.window, self.card_size, self.card_back, self.cards, self.poker, self.replace_button)
            self.draw_game.draw_scores(self.window, self.scoreboard)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #check if player clicked on a card in their hand
                        mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)    
                        for i in range(5):
                            if mouse_rect.colliderect(pygame.Rect(card_locs[i][0], \
                                                                card_locs[i][1], self.card_size[0], self.card_size[1])):
                                if self.poker.player_hand[i] not in self.poker.cards_to_replace:
                                    self.poker.cards_to_replace.append(self.poker.player_hand[i])
                                    card_locs[i] = (card_locs[i][0], card_locs[i][1] - 20)
                                    self.draw_game.update_card_loc(self.window, (self.cards[str(self.poker.player_hand[i])]), \
                                                                card_locs[i])                                              
                                else:
                                    self.poker.cards_to_replace.remove(self.poker.player_hand[i])
                                    card_locs[i] = (card_locs[i][0], card_locs[i][1] + 20)
                                    self.draw_game.update_card_loc(self.window, (self.cards[str(self.poker.player_hand[i])]), \
                                                                card_locs[i])  
                            if self.replace_button.use():
                                if len(self.poker.cards_to_replace) > 0:  
                                    self.poker.replace_cards(self.poker.cards_to_replace)
                                    self.poker.cards_to_replace = []
                                self.state = 2
                                self.running = False
                                                      
            
    def end(self):
        """
        Function that runs the end screen of the game.
        """
        self.new_round_button = Button(900, 80, 200, 100, constants.RED, "New Round", (0, 0, 0), "oldwest", 50, True)
        self.winner_nums = self.poker.get_winner()
        self.scoreboard[self.winner_nums[0]] += 1
        self.winner = self.poker.convert(self.winner_nums)
        self.end_screen = EndScreen()
        self.running = True
        #sets up a loop to make updating the screen easier
        while self.running:
            self.window.blit(self.background, (0, 0))
            self.end_screen.draw_screen(self.window, self.new_round_button, \
                                         self.poker, self.card_size, self.cards, self.winner)
            self.end_screen.draw_scores(self.window, self.scoreboard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.new_round_button.use():
                        self.poker = Poker(self.scoreboard)
                        self.state = 1
                        self.running = False

    def main(self):
        """
        Main loop of the game. Runs the game based on the state of the game.
        """
        if self.state == 0:
            self.start()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
            self.end()

