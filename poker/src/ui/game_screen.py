import constants
import pygame

class GameScreen:
    """The screen that is shown when the game is being played.
    """
    def __init__(self):
        pass

    def draw_screen(self, window, card_size, card_back, cards, poker, replace_button):
        """Draws the game screen on the screen.
        Args:
            window (pygame.Surface): the window to draw the game screen on
            card_size (tuple): the size of the cards
            card_back (pygame.Surface): the back of the cards
            cards (dict): the dictionary of the cards
            poker (Poker): the poker game
            replace_button (Button): the button to replace the cards
        """
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
        
        window.blit(pygame.font.SysFont(constants.FONT3[0], constants.FONT3[1]).render \
                    ("Select cards to replace: ", 1, constants.BLACK), \
                    (constants.WIDTH/3, \
                        constants.HEIGHT/5 - card_size[1]/2 + 110))

        replace_button.draw(window)
        
        for i in range(5):
            window.blit(cards[str(poker.player_hand[i])], self.player_card_loc[i])
            window.blit(card_back, self.bot1_card_loc[i])
            window.blit(card_back, self.bot2_card_loc[i])
            window.blit(card_back, self.bot3_card_loc[i])


    def draw_scores(self, window, scoreboard):
        """Draws the scores on the screen.
        Args:
            window (pygame.Surface): the window to draw the scores on
            scoreboard (list): the list of scores
        """
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
        
    def set_locs(self, card_size):
        """Sets the locations of the cards.
        Args:
            card_size (tuple): the size of the cards
        """
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
            
    def get_locs(self):
        """Gets the locations of the cards.
        Returns:
            list: the list of the locations of the player's cards
        """
        return self.player_card_loc

    def update_card_loc(self, window, card, card_loc):
        """Updates the location of the card.
        Args:
            window (pygame.Surface): the window to draw the card on
            card (pygame.Surface): the card to draw
            card_loc (tuple): the location of the card
        """
        window.blit(card, card_loc)
        
        
        