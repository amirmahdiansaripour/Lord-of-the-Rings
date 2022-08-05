from tkinter.tix import CELL
from turtle import width
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PIC_SIZE_X = 50
PIC_SIZE_Y = 57
GANDALF = pygame.image.load('gandalf.png')
CASTLE = pygame.image.load('castle.png')
ENEMY = pygame.image.load('enemy.png')
ORDINARY_CELL = 'o'
ENEMY_CELL = 'e'
CASTLE_CELL = 'c'
GANDALF_INITIAL = 'gi'

def getEvent():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

class Cell:
    def __init__(self, x_, y_, index_, screen_, point):
        self.x = x_
        self.y = y_
        self.Center = point
        self.rect = pygame.Rect(self.x, self.y, PIC_SIZE_Y, PIC_SIZE_X)
        self.index = index_
        self.state = ORDINARY_CELL
        self.screen = screen_
        self.gandalfHere = False
        self.font = pygame.font.SysFont('Arial', 18)
        self.inFrontier = False
        self.inExplored = False
        self.inPath = False

    def printIndex(self):
        self.screen.blit(self.font.render(str(self.index), True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))
        # self.screen.blit(self.font.render(str(self.Center), True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))
        pygame.display.update()    

    def printSetLabel(self, color, label):
        getEvent()
        pygame.draw.rect(self.screen, color, self.rect)
        self.screen.blit(self.font.render(label, True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))      
        for i in range(1):
            pygame.draw.rect(self.screen, WHITE, (self.x - i, self.y - i, PIC_SIZE_Y, PIC_SIZE_X), 1)
        pygame.display.update()


class Screen:
    def __init__(self, width, height):
        pygame.init()
        self.WIDTH = int(width) * PIC_SIZE_Y
        self.HEIGHT = int(height) * PIC_SIZE_X
        self.SCREEN = pygame.display.set_mode((int(self.WIDTH), int(self.HEIGHT)))
        
    def initField(self):
        self.table = []
        cellCounter = 0
        rowCounter = 0
        colCounter = 0
        for x in range(0, self.WIDTH, PIC_SIZE_Y):
            colCounter = 0
            for y in range(0, self.HEIGHT, PIC_SIZE_X):
                cell = Cell(x, y, cellCounter, self.SCREEN, (rowCounter, colCounter))
                self.table.append(cell)
                cellCounter += 1
                colCounter += 1
            rowCounter += 1
        return self.table

    def draw(self):
        self.SCREEN.fill(BLACK)               
        self.delay(400)
        getEvent()
        self.printIndices()
        for cell in self.table:
            pygame.draw.rect(self.SCREEN, WHITE, cell.rect, 1)
            point = (cell.x, cell.y)
            if(cell.inFrontier):
                cell.printSetLabel(RED, 'F')
            elif(cell.inPath):
                cell.printSetLabel(BLUE, '')
            if(cell.state == CASTLE_CELL):
                self.SCREEN.blit(CASTLE, point)
            elif(cell.state == ENEMY_CELL):
                self.SCREEN.blit(ENEMY, point)
            if(cell.gandalfHere):
                self.SCREEN.blit(GANDALF, point)
        pygame.display.update()    

    def delay(self, time):
        pygame.time.delay(time)
        
    def printIndices(self):
        for cell in self.table:
            getEvent()
            pygame.draw.rect(self.SCREEN, WHITE, cell.rect, 1)
            cell.printIndex()

    def drawPath(self, path):
        for index in path:
            self.table[index].inPath = True
        self.draw()

    def placePeices(self):
        self.printIndices()    
        placeOfGandalf = input("Enter gandalf place: ")
        self.table[int(placeOfGandalf)].state = GANDALF_INITIAL
        placeOfCastle = input("Enter castle place: ")
        self.table[int(placeOfCastle)].state = CASTLE_CELL
        placesOfEnemies = input("Enter places of enemies: ").split()
        for place in placesOfEnemies:
            self.table[int(place)].state = ENEMY_CELL
        self.PLACES_DONE = True
