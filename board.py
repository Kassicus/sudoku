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

        self.notes = [False, False, False, False, False, False, False, False, False, False]
        self.noted = False

        self.color = data.color.light

        self.errored = False

        self.number = 0

        self.given = False

        self.numberText = pygame.font.Font.render(data.standard, str(self.number), True, self.color)

        self.noteOneText = pygame.font.Font.render(data.note, '1', True, self.color)
        self.noteTwoText = pygame.font.Font.render(data.note, '2', True, self.color)
        self.noteThreeText = pygame.font.Font.render(data.note, '3', True, self.color)
        self.noteFourText = pygame.font.Font.render(data.note, '4', True, self.color)
        self.noteFiveText = pygame.font.Font.render(data.note, '5', True, self.color)
        self.noteSixText = pygame.font.Font.render(data.note, '6', True, self.color)
        self.noteSevenText = pygame.font.Font.render(data.note, '7', True, self.color)
        self.noteEightText = pygame.font.Font.render(data.note, '8', True, self.color)
        self.noteNineText = pygame.font.Font.render(data.note, '9', True, self.color)

    def update(self):
        self.checkMouse()
        self.checkKeyboard()

        if self.errored:
            self.color = data.color.error
        else:
            self.color = data.color.light

        if self.given:
            self.color = data.color.select

        if self.noted:
            self.color = data.color.note

        self.numberText = pygame.font.Font.render(data.standard, str(self.number), True, self.color)

        self.noteOneText = pygame.font.Font.render(data.note, '1', True, self.color)
        self.noteTwoText = pygame.font.Font.render(data.note, '2', True, self.color)
        self.noteThreeText = pygame.font.Font.render(data.note, '3', True, self.color)
        self.noteFourText = pygame.font.Font.render(data.note, '4', True, self.color)
        self.noteFiveText = pygame.font.Font.render(data.note, '5', True, self.color)
        self.noteSixText = pygame.font.Font.render(data.note, '6', True, self.color)
        self.noteSevenText = pygame.font.Font.render(data.note, '7', True, self.color)
        self.noteEightText = pygame.font.Font.render(data.note, '8', True, self.color)
        self.noteNineText = pygame.font.Font.render(data.note, '9', True, self.color)

    def draw(self, surface):
        if self.hovered:
            self.drawHover(surface)

        if self.selected:
            surface.blit(self.selectedImage, (self.x, self.y))

        if self.number != 0:
            surface.blit(self.numberText, (self.x + 27, self.y + 10))

        if self.notes[1]:
            surface.blit(self.noteOneText, (self.x + 8, self.y))
        if self.notes[2]:
            surface.blit(self.noteTwoText, (self.x + 33, self.y))
        if self.notes[3]:
            surface.blit(self.noteThreeText, (self.x + 58, self.y))
        if self.notes[4]:
            surface.blit(self.noteFourText, (self.x + 8, self.y + 25))
        if self.notes[5]:
            surface.blit(self.noteFiveText, (self.x + 33, self.y + 25))
        if self.notes[6]:
            surface.blit(self.noteSixText, (self.x + 58, self.y + 25))
        if self.notes[7]:
            surface.blit(self.noteSevenText, (self.x + 8, self.y + 50))
        if self.notes[8]:
            surface.blit(self.noteEightText, (self.x + 33, self.y + 50))
        if self.notes[9]:
            surface.blit(self.noteNineText, (self.x + 58, self.y + 50))

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
                    if data.writemode == 'given':
                        self.given = True
                        self.noted = False

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

                    elif data.writemode == 'normal':
                        self.given = False
                        self.noted = False

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

                    if data.writemode == 'note':
                        self.noted = True
                        if event.key == pygame.K_0:
                            if self.notes[0]:
                                self.notes[0] = False
                            else:
                                self.notes[0] = True
                        if event.key == pygame.K_1:
                            if self.notes[1]:
                                self.notes[1] = False
                            else:
                                self.notes[1] = True
                        if event.key == pygame.K_2:
                            if self.notes[2]:
                                self.notes[2] = False
                            else:
                                self.notes[2] = True
                        if event.key == pygame.K_3:
                            if self.notes[3]:
                                self.notes[3] = False
                            else:
                                self.notes[3] = True
                        if event.key == pygame.K_4:
                            if self.notes[4]:
                                self.notes[4] = False
                            else:
                                self.notes[4] = True
                        if event.key == pygame.K_5:
                            if self.notes[5]:
                                self.notes[5] = False
                            else:
                                self.notes[5] = True
                        if event.key == pygame.K_6:
                            if self.notes[6]:
                                self.notes[6] = False
                            else:
                                self.notes[6] = True
                        if event.key == pygame.K_7:
                            if self.notes[7]:
                                self.notes[7] = False
                            else:
                                self.notes[7] = True
                        if event.key == pygame.K_8:
                            if self.notes[8]:
                                self.notes[8] = False
                            else:
                                self.notes[8] = True
                        if event.key == pygame.K_9:
                            if self.notes[9]:
                                self.notes[9] = False
                            else:
                                self.notes[9] = True


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
                    self.cells[cell].errored = True
                else:
                    numbers.append(self.cells[cell].number)
                    self.cells[cell].errored = False

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

        #self.checkRows(self.regions['Region One'], self.regions['Region Two'], self.regions['Region Three'])
        #self.checkRows(self.regions['Region Four'], self.regions['Region Five'], self.regions['Region Six'])
        #self.checkRows(self.regions['Region Seven'], self.regions['Region Eight'], self.regions['Region Nine'])

        #self.checkColumns(self.regions['Region One'], self.regions['Region Four'], self.regions['Region Seven'])
        #self.checkColumns(self.regions['Region Two'], self.regions['Region Five'], self.regions['Region Eight'])
        #self.checkColumns(self.regions['Region Three'], self.regions['Region Six'], self.regions['Region Nine'])

    def checkRows(self, r1, r2, r3):
        for checkRow in range(3):
            numbers = []

            for x in range(len(r1.rows[checkRow])):
                if r1.rows[checkRow][x].number != 0:
                    if r1.rows[checkRow][x].number in numbers:
                        r1.rows[checkRow][x].errored = True
                    else:
                        numbers.append(r1.rows[checkRow][x].number)
                        r1.rows[checkRow][x].errored = False

            for x in range(len(r2.rows[checkRow])):
                if r2.rows[checkRow][x].number != 0:
                    if r2.rows[checkRow][x].number in numbers:
                        r2.rows[checkRow][x].errored = True
                    else:
                        numbers.append(r2.rows[checkRow][x].number)
                        r2.rows[checkRow][x].errored = False

            for x in range(len(r3.rows[checkRow])):
                if r3.rows[checkRow][x].number != 0:
                    if r3.rows[checkRow][x].number in numbers:
                        r3.rows[checkRow][x].errored = True
                    else:
                        numbers.append(r3.rows[checkRow][x].number)
                        r3.rows[checkRow][x].errored = False

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
