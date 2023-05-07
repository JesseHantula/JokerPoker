import pygame
import constants
from ui.game_screen import GameScreen

class EndScreen:
    def __init__(self):
        pass

    def draw_screen(self, window, new_round_button, poker, card_size, cards, winner):
        window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                    ("You", 1, constants.BLACK), (constants.WIDTH/3 + 150, \
                                                   constants.HEIGHT/5 - card_size[1]/2 - 50))
            
        window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                    ("Bot 1", 1, constants.BLACK), (constants.WIDTH/3 - card_size[0]/2 - 300 + 175, \
                                                    constants.HEIGHT/5 - card_size[1]/2 + 200))
        
        window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                    ("Bot 2", 1, constants.BLACK), ((constants.WIDTH/3 - card_size[0]/2 - 300 + 175) + 650, \
                                                    constants.HEIGHT/5 - card_size[1]/2 + 200))
        
        window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                    ("Bot 3", 1, constants.BLACK), (constants.WIDTH/3 - card_size[0]/2 + 175, \
                                                    constants.HEIGHT/5 - card_size[1]/2 + 450))
        self.set_locs(card_size)
        for i in range(5):
            window.blit(cards[str(poker.player_hand[i])], self.player_card_loc[i])
            window.blit(cards[str(poker.bot1_hand[i])], self.bot1_card_loc[i])
            window.blit(cards[str(poker.bot2_hand[i])], self.bot2_card_loc[i])
            window.blit(cards[str(poker.bot3_hand[i])], self.bot3_card_loc[i])
        if winner[0] == "You":
            window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                    (winner[0] + " win with " + winner[1] + "!", 1, constants.WHITE), \
                    (constants.WIDTH/2 - 200, constants.HEIGHT/2 - 150))
        else:
            window.blit(pygame.font.SysFont(constants.FONT2[0], constants.FONT2[1]).render \
                        (winner[0] + " wins with " + winner[1] + "!", 1, constants.WHITE), \
                        (constants.WIDTH/2 - 200, constants.HEIGHT/2 - 150))
        
        new_round_button.draw(window)
        

    def set_locs(self, card_size):
        self.player_card_loc = []
        for i in range(5):
            self.player_card_loc.append(
                (constants.WIDTH/3 - card_size[0]/2 + i * 100, constants.HEIGHT/5 - card_size[1]/2))

        self.bot1_card_loc = []
        for i in range(5):
            self.bot1_card_loc.append(
                ((constants.WIDTH/3 - card_size[0]/2 - 300 + i * 100), \
                 constants.HEIGHT/5 - card_size[1]/2 + 250))

        self.bot2_card_loc = []
        for i in range(5):
            self.bot2_card_loc.append(
                (constants.WIDTH/3 - card_size[0]/2 - 300 + i * 100 + 650, \
                 constants.HEIGHT/5 - card_size[1]/2 + 250))

        self.bot3_card_loc = []
        for i in range(5):
            self.bot3_card_loc.append(
                (constants.WIDTH/3 - card_size[0]/2 + i * 100, constants.HEIGHT/5 - card_size[1]/2 + 500))
            
    def draw_scores(self, window, scoreboard):
        window.blit(pygame.font.SysFont(constants.FONT3[0], constants.FONT3[1]).render \
                         (f"Your score: {scoreboard[0]}", 1, constants.BLACK), \
                         (20, 20))
        
        window.blit(pygame.font.SysFont(constants.FONT3[0], constants.FONT3[1]).render \
                            (f"Bot 1 score: {scoreboard[1]}", 1, constants.BLACK), \
                            (20, 55))
        
        window.blit(pygame.font.SysFont(constants.FONT3[0], constants.FONT3[1]).render \
                            (f"Bot 2 score: {scoreboard[2]}", 1, constants.BLACK), \
                            (20, 90))
        
        window.blit(pygame.font.SysFont(constants.FONT3[0], constants.FONT3[1]).render \
                            (f"Bot 3 score: {scoreboard[3]}", 1, constants.BLACK), \
                            (20, 125))
        
        pygame.display.update()