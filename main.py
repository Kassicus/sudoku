import pygame
import os
import data

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

hostInfo = pygame.display.Info()

class Game(object):
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

        self.running = True
        self.clock = pygame.time.Clock()
        data.events = pygame.event.get()

    def start(self):
        while self.running:
            data.events = pygame.event.get()

            for event in data.events:
                if event.type == pygame.QUIT:
                    running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.color.black)

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

game = Game(800, 800, "Kassicus/sudoku")
game.start()

pygame.quit()
