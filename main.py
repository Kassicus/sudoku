import pygame
import os
import data
import board

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

        self.board = board.Board()

    def start(self):
        while self.running:
            data.events = pygame.event.get()

            for event in data.events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        data.writemode = data.writemodes[2]
                    if event.key == pygame.K_a:
                        data.writemode = data.writemodes[0]
                    if event.key == pygame.K_d:
                        data.writemode = data.writemodes[1]

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.color.black)

        self.board.draw(self.screen)

    def update(self):
        self.board.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(758, 758, "Kassicus/sudoku")
game.start()

pygame.quit()
