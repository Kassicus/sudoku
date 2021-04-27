import pygame
import data

class Cell(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.hovered = False

    def update(self):
        self.checkMouse()

    def draw(self, surface):
        if self.hovered:
            self.drawHover(surface)

    def drawOutline(self, surface):
        pygame.draw.rect(surface, data.color.green, (self.x, self.y, self.width, self.height), 1)

    def drawHover(self, surface):
        pygame.draw.rect(surface, data.color.highlight, (self.x, self.y, self.width, self.height))

    def checkMouse(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False


class Region(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.cells = {
        'Cell One': Cell(self.x + 0, self.y + 0, 80, 80),
        'Cell Two': Cell(self.x + 83, self.y + 0, 80, 80),
        'Cell Three': Cell(self.x + 166, self.y + 0, 80, 80),
        'Cell Four': Cell(self.x + 0, self.y + 83, 80, 80),
        'Cell Five': Cell(self.x + 83, self.y + 83, 80, 80),
        'Cell Six': Cell(self.x + 166, self.y + 83, 80, 80),
        'Cell Seven': Cell(self.x + 0, self.y + 166, 80, 80),
        'Cell Eight': Cell(self.x + 83, self.y + 166, 80, 80),
        'Cell Nine': Cell(self.x + 166, self.y + 166, 80, 80)
        }

    def update(self):
        for cell in self.cells:
            self.cells[cell].update()

    def draw(self, surface):
        for cell in self.cells:
            self.cells[cell].draw(surface)

    def drawOutline(self, surface):
        pygame.draw.rect(surface, data.color.white, (self.x, self.y, self.width, self.height), 1)

class Board(object):
    def __init__(self):
        self.x = 0
        self.y = 0

        self.backgroundImage = pygame.image.load('assets/board/background.png')

        self.regions = {
        'Region One': Region(5, 5, 246, 246),
        'Region Two': Region(256, 5, 246, 246),
        'Region Three': Region(507, 5, 246, 246),
        'Region Four': Region(5, 256, 246, 246),
        'Region Five': Region(256, 256, 246, 246),
        'Region Six': Region(507, 256, 246, 246),
        'Region Seven': Region(5, 507, 246, 246),
        'Region Eight': Region(256, 507, 246, 246),
        'Region Nine': Region(507, 507, 246, 246)
        }

    def update(self):
        for region in self.regions:
            self.regions[region].update()

    def draw(self, surface):
        surface.blit(self.backgroundImage, (self.x, self.y))

        for region in self.regions:
            self.regions[region].draw(surface)
