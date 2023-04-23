"""
this module is the main module of the game
"""
import sys
import pygame
from entities.models import Deck
from entities.engine import Poker


HEIGHT = 720
WIDTH = 1280

# global colors that are used
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        self.deck = Deck()
        self.scale = 0.75
        self.card_size = (WIDTH * 0.1, HEIGHT * 0.2)
        self.cards = {}
        self.card_back = pygame.image.load(
            "src/images/cards/BACK.png").convert_alpha()
        scaled_width = int(self.scale * self.card_size[0])
        scaled_height = int(self.scale * self.card_size[1])
        self.card_back = pygame.transform.scale(
            self.card_back, (scaled_width, scaled_height))
        self.background = pygame.image.load("src/images/background.jpg")
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT))
        self.window.blit(self.background, (0, 0))

        pygame.display.flip()

        for card in self.deck.cards:
            self.cards[str(card)] = pygame.transform.scale(
                card.image, (scaled_width, scaled_height))

        self.start_up_init()

    def start_up_init(self):
        self.scoreboard = [0, 0, 0, 0]
        self.poker = Poker(self.scoreboard)

        self.font1 = pygame.font.SysFont("oldwest", 100)
        self.font2 = pygame.font.SysFont("comicsans", 50)
        self.font3 = pygame.font.SysFont("comicsans", 30)
        self.start_text = self.font1.render("Joker Poker", 1, black)
        self.start_text_loc = (WIDTH/2 - self.start_text.get_width()/2,
                               HEIGHT/2 - self.start_text.get_height()/2 - 100)
        self.start_button = self.font2.render("Start", 1, red)
        self.start_button_loc = (WIDTH/2 - self.start_button.get_width()/2,
                                 HEIGHT/2 - self.start_button.get_height()/2)
        self.button = pygame.Rect(self.start_button_loc[0], self.start_button_loc[1],
                                  self.start_button.get_width(), self.start_button.get_height())
        self.state = 0

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.play_init()
                    self.state += 1

        self.window.blit(self.start_text, self.start_text_loc)
        self.window.blit(self.start_button, self.start_button_loc)

        pygame.display.update()

    def play_init(self):
        # set location for cards in our hand (5 cards)
        self.player_card_loc = []
        for i in range(5):
            self.player_card_loc.append(
                (WIDTH/3 - self.card_size[0]/2 + i * 100, HEIGHT/5 - self.card_size[1]/2))

        self.bot1_card_loc = []
        for i in range(5):
            self.bot1_card_loc.append(
                ((WIDTH/3 - self.card_size[0]/2 - 300 + i * 100) + 650, \
                 HEIGHT/5 - self.card_size[1]/2 + 250))

        self.bot2_card_loc = []
        for i in range(5):
            self.bot2_card_loc.append(
                (WIDTH/3 - self.card_size[0]/2 - 300 + i * 100, \
                 HEIGHT/5 - self.card_size[1]/2 + 250))

        self.bot3_card_loc = []
        for i in range(5):
            self.bot3_card_loc.append(
                (WIDTH/3 - self.card_size[0]/2 + i * 100, HEIGHT/5 - self.card_size[1]/2 + 500))

        # set location for text above each player's hand
        self.player_text = self.font2.render("You", 1, black)
        self.player_text_loc = (
            WIDTH/3 - self.player_text.get_width()/2 + 175, HEIGHT/5 - self.card_size[1]/2 - 75)
        self.bot1_text = self.font2.render("Bot 1", 1, black)
        self.bot1_text_loc = (
            WIDTH/3 - self.card_size[0]/2 - 300 + 175, HEIGHT/5 - self.card_size[1]/2 + 175)
        self.bot2_text = self.font2.render("Bot 2", 1, black)
        self.bot2_text_loc = (
            (WIDTH/3 - self.card_size[0]/2 - 300 + 175) + 650, HEIGHT/5 - self.card_size[1]/2 + 175)
        self.bot3_text = self.font2.render("Bot 3", 1, black)
        self.bot3_text_loc = (
            WIDTH/3 - self.card_size[0]/2 + 175, HEIGHT/5 - self.card_size[1]/2 + 425)

        # set location for text below player's hand
        self.player_hand_text = self.font3.render(
            "Select cards to replace: ", 1, black)
        self.player_hand_text_loc = (
            WIDTH/3 - self.player_hand_text.get_width()/2 + 185, \
            HEIGHT/5 - self.card_size[1]/2 + 110)

        # make replace button
        self.replace_button = self.font2.render("Replace", 1, red)
        self.replace_button_loc = (
            WIDTH/3 - self.replace_button.get_width()/2 + 550, HEIGHT/5 - self.card_size[1]/2 + 10)

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #check if player clicked on a card in their hand
                    mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    for i in range(5):
                        if mouse_rect.colliderect(pygame.Rect(self.player_card_loc[i][0], \
                                                              self.player_card_loc[i][1], self.card_size[0], self.card_size[1])):
                            if self.poker.player_hand[i] not in self.poker.cards_to_replace:
                                self.poker.cards_to_replace.append(
                                    self.poker.player_hand[i])
                                self.player_card_loc[i] = (
                                    self.player_card_loc[i][0], self.player_card_loc[i][1] - 20)
                            else:
                                self.poker.cards_to_replace.remove(
                                    self.poker.player_hand[i])
                                self.player_card_loc[i] = (
                                    self.player_card_loc[i][0], self.player_card_loc[i][1] + 20)

                    # check if player clicked on the replace button, if so, replace the cards
                    if mouse_rect.colliderect(pygame.Rect(self.replace_button_loc[0], \
                                                          self.replace_button_loc[1], self.replace_button.get_width(), self.replace_button.get_height())):
                        self.poker.replace_cards(self.poker.cards_to_replace)
                        self.poker.cards_to_replace = []
                        self.end_init()
                        self.state += 1

        self.window.blit(self.background, (0, 0))

        # display cards in our hand
        for i in range(5):
            self.window.blit(
                self.cards[str(self.poker.player_hand[i])], self.player_card_loc[i])
            self.window.blit(self.card_back, self.bot1_card_loc[i])
            self.window.blit(self.card_back, self.bot2_card_loc[i])
            self.window.blit(self.card_back, self.bot3_card_loc[i])

        # display text above each player's hand
        self.window.blit(self.player_text, self.player_text_loc)
        self.window.blit(self.bot1_text, self.bot1_text_loc)
        self.window.blit(self.bot2_text, self.bot2_text_loc)
        self.window.blit(self.bot3_text, self.bot3_text_loc)

        # display text below player's hand
        self.window.blit(self.player_hand_text, self.player_hand_text_loc)

        # display replace button
        self.window.blit(self.replace_button, self.replace_button_loc)

        # call function that displays scores
        self.scores()
        pygame.display.update()

    def end(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # check if player clicked on the play again button, if so, reset the game
                    mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                    if mouse_rect.colliderect(pygame.Rect(self.new_game_button_loc[0], \
                                                          self.new_game_button_loc[1], self.new_game_button.get_width(), self.new_game_button.get_height())):
                        self.poker.reset()
                        self.poker.deal()
                        self.init()
                        self.state = 1

        self.window.blit(self.background, (0, 0))

        # display cards in our hand
        for i in range(5):
            self.window.blit(
                self.cards[str(self.poker.player_hand[i])], self.player_card_loc[i])
            self.window.blit(
                self.cards[str(self.poker.bot1_hand[i])], self.bot1_card_loc[i])
            self.window.blit(
                self.cards[str(self.poker.bot2_hand[i])], self.bot2_card_loc[i])
            self.window.blit(
                self.cards[str(self.poker.bot3_hand[i])], self.bot3_card_loc[i])

        # display text above each player's hand
        self.window.blit(self.player_text, self.player_text_loc)
        self.window.blit(self.bot1_text, self.bot1_text_loc)
        self.window.blit(self.bot2_text, self.bot2_text_loc)
        self.window.blit(self.bot3_text, self.bot3_text_loc)

        # display play again button
        self.window.blit(self.new_game_button, self.new_game_button_loc)

        # call function that displays scores
        self.scores()
        pygame.display.update()

    def end_init(self):
        # set location for text above each player's hand
        self.player_text = self.font2.render("You", 1, black)
        self.player_text_loc = (
            WIDTH/3 - self.player_text.get_width()/2 + 175, HEIGHT/5 - self.card_size[1]/2 - 75)
        self.bot1_text = self.font2.render("Bot 1", 1, black)
        self.bot1_text_loc = (
            WIDTH/3 - self.card_size[0]/2 - 300 + 175, HEIGHT/5 - self.card_size[1]/2 + 175)
        self.bot2_text = self.font2.render("Bot 2", 1, black)
        self.bot2_text_loc = (
            (WIDTH/3 - self.card_size[0]/2 - 300 + 175) + 650, HEIGHT/5 - self.card_size[1]/2 + 175)
        self.bot3_text = self.font2.render("Bot 3", 1, black)
        self.bot3_text_loc = (
            WIDTH/3 - self.card_size[0]/2 + 175, HEIGHT/5 - self.card_size[1]/2 + 425)

        # make new game button
        self.new_game_button = self.font2.render("New Round", 1, red)
        self.new_game_button_loc = (
            WIDTH/3 - self.replace_button.get_width()/2 + 550, HEIGHT/5 - self.card_size[1]/2 + 10)

    def scores(self):
        # display scores
        self.player_score = self.font3.render(
            f"Your score: {self.scoreboard[0]}", 1, black)
        self.player_score_loc = (
            WIDTH/3 - self.card_size[0]/2 - 330, HEIGHT/5 - self.card_size[1]/2-35)
        self.bot1_score = self.font3.render(
            f"Bot 1 score: {self.scoreboard[1]}", 1, black)
        self.bot1_score_loc = (
            WIDTH/3 - self.card_size[0]/2 - 330, HEIGHT/5 - self.card_size[1]/2)
        self.bot2_score = self.font3.render(
            f"Bot 2 score: {self.scoreboard[2]}", 1, black)
        self.bot2_score_loc = (
            WIDTH/3 - self.card_size[0]/2 - 330, HEIGHT/5 - self.card_size[1]/2 + 35)
        self.bot3_score = self.font3.render(
            f"Bot 3 score: {self.scoreboard[3]}", 1, black)
        self.bot3_score_loc = (
            WIDTH/3 - self.card_size[0]/2 - 330, HEIGHT/5 - self.card_size[1]/2 + 70)

        self.window.blit(self.player_score, self.player_score_loc)
        self.window.blit(self.bot1_score, self.bot1_score_loc)
        self.window.blit(self.bot2_score, self.bot2_score_loc)
        self.window.blit(self.bot3_score, self.bot3_score_loc)

    def main(self):
        if self.state == 0:
            self.start()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
            self.end()

