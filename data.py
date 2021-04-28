import pygame

pygame.font.init()

events = None

class Colors():
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.highlight = (44, 42, 67)
        self.light = (203, 219, 252)
        self.error = (236, 29, 116)
        self.select = (55, 148, 110)
        self.note = (95, 95, 95)

color = Colors()

standard = pygame.font.Font('assets/fonts/JetBrainsMono-Regular.ttf', 48)
note = pygame.font.Font('assets/fonts/JetBrainsMono-Regular.ttf', 24)

writemodes = ['normal', 'note', 'given']
writemode = 'normal'
