import pygame
from .button import Button
import constants

class StartScreen:
    def __init__(self):
        pass

    def draw_screen(self, window, start_button):       
        window.blit(pygame.font.SysFont(constants.FONT1[0], constants.FONT1[1]).render \
                    ("JOKER POKER", 1, constants.BLACK), (constants.WIDTH/2 - 250, 200))
        start_button.draw(window)
        pygame.display.update()