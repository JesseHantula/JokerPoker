import pygame
from ui.game_ui import Game

WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption("POKER")
    Run = Game()
    while True:
        Run.main()
