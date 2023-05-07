import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font, font_size, usable):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, font_size)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.usable = usable

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, self.text_color)
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), \
                           self.y + (self.height/2 - text.get_height()/2)))
        
    def use(self):
        if self.usable:
            mousepos = pygame.mouse.get_pos()
            if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
                return True
        