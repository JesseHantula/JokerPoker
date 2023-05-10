import pygame
import constants

class StartScreen:
    """
    Class that draws the start screen.
    """
    def __init__(self):
        pass

    def draw_screen(self, window, start_button):    
        """Draws the start screen on the screen.
        Args:
            window (pygame.Surface): the window to draw the start screen on
            start_button (Button): the start button
        """   
        window.blit(pygame.font.SysFont(constants.FONT1[0], constants.FONT1[1]).render \
                    ("JOKER POKER", 1, constants.BLACK), (constants.WIDTH/2 - 250, 200))
        start_button.draw(window)
        pygame.display.update()