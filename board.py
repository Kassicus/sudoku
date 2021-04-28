import pygame
import data

class Cell(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.selectedImage = pygame.image.load('assets/board/selected_indicator.png')

        self.hovered = False
        self.selected = False

        self.notes = []
        self.noted = False

        self.number = 0

        self.numberText = pygame.font.Font.render(data.standard, str(self.number), True, data.color.light)

    def update(self):
        self.checkMouse()
        self.checkKeyboard()

        self.numberText = pygame.font.Font.render(data.standard, str(self.number), True, data.color.light)

    def draw(self, surface):
        if self.hovered:
            self.drawHover(surface)

        if self.selected:
            surface.blit(self.selectedImage, (self.x, self.y))

        if self.number != 0:
            surface.blit(self.numberText, (self.x + 27, self.y + 10))

    def drawOutline(self, surface):
        pygame.draw.rect(surface, data.color.green, (self.x, self.y, self.width, self.height), 1)

    def drawHover(self, surface):
        pygame.draw.rect(surface, data.color.highlight, (self.x, self.y, self.width, self.height))

    def checkMouse(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.x <= mouse_pos[0] <= self.x + self.width:
            if self.y <= mouse_pos[1] <= self.y + self.height:
                self.hovered = True
                self.checkClicked(True)
            else:
                self.hovered = False
                self.checkClicked(False)
        else:
            self.hovered = False
            self.checkClicked(False)

    def checkClicked(self, flag):
        for event in data.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = flag

    def checkKeyboard(self):
        if self.selected:
            for event in data.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.number = 0
                    if event.key == pygame.K_1:
                        self.number = 1
                    if event.key == pygame.K_2:
                        self.number = 2
                    if event.key == pygame.K_3:
                        self.number = 3
                    if event.key == pygame.K_4:
                        self.number = 4
                    if event.key == pygame.K_5:
                        self.number = 5
                    if event.key == pygame.K_6:
                        self.number = 6
                    if event.key == pygame.K_7:
                        self.number = 7
                    if event.key == pygame.K_8:
                        self.number = 8
                    if event.key == pygame.K_9:
                        self.number = 9


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

        self.rows = [
        [self.cells['Cell One'], self.cells['Cell Two'], self.cells['Cell Three']],
        [self.cells['Cell Four'], self.cells['Cell Five'], self.cells['Cell Six']],
        [self.cells['Cell Seven'], self.cells['Cell Eight'], self.cells['Cell Nine']]
        ]

        self.columns = [
        [self.cells['Cell One'], self.cells['Cell Four'], self.cells['Cell Seven']],
        [self.cells['Cell Two'], self.cells['Cell Five'], self.cells['Cell Eight']],
        [self.cells['Cell Three'], self.cells['Cell Six'], self.cells['Cell Nine']]
        ]

    def update(self):
        for cell in self.cells:
            self.cells[cell].update()

    def draw(self, surface):
        for cell in self.cells:
            self.cells[cell].draw(surface)

    def drawOutline(self, surface):
        pygame.draw.rect(surface, data.color.white, (self.x, self.y, self.width, self.height), 1)

    def checkDuplicates(self):
        numbers = []

        for cell in self.cells:
            if self.cells[cell].number != 0:
                if self.cells[cell].number in numbers:
                    print('error')
                else:
                    numbers.append(self.cells[cell].number)

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

        self.checkDuplicates()

    def draw(self, surface):
        surface.blit(self.backgroundImage, (self.x, self.y))

        for region in self.regions:
            self.regions[region].draw(surface)

    def checkDuplicates(self):
        for region in self.regions:
            self.regions[region].checkDuplicates()

        self.checkRows(self.regions['Region One'], self.regions['Region Two'], self.regions['Region Three'])
        self.checkRows(self.regions['Region Four'], self.regions['Region Five'], self.regions['Region Six'])
        self.checkRows(self.regions['Region Seven'], self.regions['Region Eight'], self.regions['Region Nine'])

        self.checkColumns(self.regions['Region One'], self.regions['Region Four'], self.regions['Region Seven'])
        self.checkColumns(self.regions['Region Two'], self.regions['Region Five'], self.regions['Region Eight'])
        self.checkColumns(self.regions['Region Three'], self.regions['Region Six'], self.regions['Region Nine'])

    def checkRows(self, r1, r2, r3):
        for checkRow in range(3):
            numbers = []

            for x in range(len(r1.rows[checkRow])):
                if r1.rows[checkRow][x].number != 0:
                    if r1.rows[checkRow][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r1.rows[checkRow][x].number)

            for x in range(len(r2.rows[checkRow])):
                if r2.rows[checkRow][x].number != 0:
                    if r2.rows[checkRow][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r2.rows[checkRow][x].number)

            for x in range(len(r3.rows[checkRow])):
                if r3.rows[checkRow][x].number != 0:
                    if r3.rows[checkRow][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r3.rows[checkRow][x].number)

    def checkColumns(self, r1, r2, r3):
        for checkColumn in range(3):
            numbers = []

            for x in range(len(r1.columns[checkColumn])):
                if r1.columns[checkColumn][x].number != 0:
                    if r1.columns[checkColumn][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r1.columns[checkColumn][x].number)

            for x in range(len(r2.columns[checkColumn])):
                if r2.columns[checkColumn][x].number != 0:
                    if r2.columns[checkColumn][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r2.columns[checkColumn][x].number)

            for x in range(len(r3.columns[checkColumn])):
                if r3.columns[checkColumn][x].number != 0:
                    if r3.columns[checkColumn][x].number in numbers:
                        print('error')
                    else:
                        numbers.append(r3.columns[checkColumn][x].number)
