from tkinter.tix import CELL
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
PIC_SIZE_X = 50
PIC_SIZE_Y = 57
GANDALF = pygame.image.load('gandalf.png')
ALLY = pygame.image.load('ally.png')
CASTLE = pygame.image.load('castle.png')
ENEMY = pygame.image.load('enemy.png')
ORDINARY_CELL = 'o'
ALLY_CELL = 'a'
ENEMY_CELL = 'e'
CASTLE_CELL = 'c'
GANDALF_CELL = 'g'


class Cell:
    def __init__(self, x_, y_, index_, screen_):
        self.x = x_
        self.y = y_
        self.rect = pygame.Rect(self.x, self.y, PIC_SIZE_Y, PIC_SIZE_X)
        self.index = index_
        self.state = ORDINARY_CELL
        self.screen = screen_
        self.font = pygame.font.SysFont('Arial', 18)
    def printIndex(self):
        self.screen.blit(self.font.render(str(self.index), True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))
        pygame.display.update()    

class Screen:
    def __init__(self):
        self.CELLS = []

    def initField(self):
        self.NUM_OF_CELLS = 0
        for x in range(0, self.WIDTH, PIC_SIZE_Y):
            for y in range(0, self.HEIGHT, PIC_SIZE_X):
                cell = Cell(x, y, self.NUM_OF_CELLS, self.SCREEN)
                self.CELLS.append(cell)
                self.NUM_OF_CELLS += 1

    def draw(self):
        for cell in self.CELLS:
            pygame.draw.rect(self.SCREEN, WHITE, cell.rect, 1)
            point = (cell.x, cell.y)
            if(cell.state == GANDALF_CELL):
                self.SCREEN.blit(GANDALF, point)
            elif(cell.state == ALLY_CELL):
                self.SCREEN.blit(ALLY, point)
            elif(cell.state == CASTLE_CELL):
                self.SCREEN.blit(CASTLE, point)
            elif(cell.state == ENEMY_CELL):
                self.SCREEN.blit(ENEMY, point)

    def printIndices(self):
        for cell in self.CELLS:
            cell.printIndex()


    def placePeices(self):
        self.printIndices()
        placeOfGandalf = input("Enter gandalf place: ")
        self.CELLS[int(placeOfGandalf)].state = GANDALF_CELL
        placeOfCastle = input("Enter castle place: ")
        self.CELLS[int(placeOfCastle)].state = CASTLE_CELL
        placesOfAllies = input("Enter places of allies: ").split()
        for place in placesOfAllies:
            self.CELLS[int(place)].state = ALLY_CELL
        placesOfEnemies = input("Enter places of enemies: ").split()
        for place in placesOfEnemies:
            self.CELLS[int(place)].state = ENEMY_CELL
        self.SCREEN.fill(BLACK)               
        self.PLACES_DONE = True


    def flow(self):
        self.PLACES_DONE = False
        pygame.init()
        # numOfRows, numOfCols = input("Enter number of rows and columns: ").split()
        numOfRows, numOfCols = 10, 15
        self.WIDTH = int(numOfCols) * PIC_SIZE_Y
        self.HEIGHT = int(numOfRows) * PIC_SIZE_X
        self.SCREEN = pygame.display.set_mode((int(self.WIDTH), int(self.HEIGHT)))
        self.initField()
        while(True):
            self.draw()
            if(self.PLACES_DONE == False):
                self.placePeices()
            pygame.display.update()

            
screen = Screen()
screen.flow()