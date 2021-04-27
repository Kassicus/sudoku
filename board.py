import pygame

class Cell(object):
    def __init__(self):
        pass

class Region(object):
    def __init__(self):
        pass

class Board(object):
    def __init__(self):
        self.x = 0
        self.y = 0

        self.backgroundImage = pygame.image.load('assets/board/background.png')

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.backgroundImage, (self.x, self.y))
