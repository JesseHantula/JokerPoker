import pygame

class Button:
    """Class that represents a button.
    Attributes:
        x (int): x position of the button
        y (int): y position of the button
        width (int): width of the button
        height (int): height of the button
        color (tuple): color of the button
        text (str): text of the button
        text_color (tuple): color of the text
        font (str): font of the text
        font_size (int): size of the font
        usable (bool): whether the button is usable or not
    """
    def __init__(self, x, y, width, height, color, text, text_color, font, font_size, usable):
        """Constructor class that initializes the button.
        Args:
            x (int): x position of the button
            y (int): y position of the button
            width (int): width of the button
            height (int): height of the button
            color (tuple): color of the button
            text (str): text of the button
            text_color (tuple): color of the text
            font (str): font of the text
            font_size (int): size of the font
            usable (bool): whether the button is usable or not
        """
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
        """Draws the button on the screen.
        Args:
            window (pygame.Surface): the window to draw the button on
        """
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, self.text_color)
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), \
                           self.y + (self.height/2 - text.get_height()/2)))
        
    def use(self):
        """Uses the button. 
        Returns:
            True if the button has been clicked.
        """
        if self.usable:
            mousepos = pygame.mouse.get_pos()
            if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
                return True
