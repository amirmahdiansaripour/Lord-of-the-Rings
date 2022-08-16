from tkinter.tix import CELL
from turtle import width
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
PIC_SIZE_X = 50
PIC_SIZE_Y = 57
GANDALF = pygame.image.load('gandalf.png')
CASTLE = pygame.image.load('castle.png')
ENEMY = pygame.image.load('enemy.png')

def getEvent():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

class Cell:
    def __init__(self, x_, y_, index_, screen_, point):
        self.x = x_
        self.y = y_
        self.center = point
        self.rect = pygame.Rect(self.x, self.y, PIC_SIZE_Y, PIC_SIZE_X)
        self.index = index_
        self.screen = screen_
        self.gandalfHere = False
        self.castleHere = False
        self.enemyHere = False
        self.font = pygame.font.SysFont('Arial', 18)
        self.inFrontier = False
        self.inExplored = False
        self.inPath = False
        self.placing = False
        self.stage = 0
        self.label = ''
        self.gandalfInitPlace = False
        self.cost = 0
        self.repeatedState = False

    def printIndex(self):
        self.screen.blit(self.font.render(str(self.cost), True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))
        # self.screen.blit(self.font.render(str(self.center), True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))
        pygame.display.update()    

    def printSetLabel(self, color):
        getEvent()
        pygame.draw.rect(self.screen, color, self.rect)
        self.screen.blit(self.font.render(self.label, True, WHITE), (self.x - 10 + (PIC_SIZE_X // 2), self.y - 10 + (PIC_SIZE_Y // 2)))      
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

    def quit(self):
        # pygame.quit()
        return

    def draw(self):
        self.SCREEN.fill(BLACK)               
        self.delay(DELAY_TIME)
        self.printIndices()
        getEvent()
        for cell in self.table:
            pygame.draw.rect(self.SCREEN, WHITE, cell.rect, 1)
            point = (cell.x, cell.y)
            if(cell.inFrontier):
                cell.label = str(cell.cost)
                cell.printSetLabel(RED)
            elif(cell.inExplored):
                cell.label = str(cell.cost)
                cell.printSetLabel(BLUE)
            elif(cell.inPath):
                cell.label = str(cell.stage)
                cell.printSetLabel(BLUE)
            elif(cell.placing):
                cell.printSetLabel(PINK)
            elif(cell.repeatedState):
                cell.printSetLabel(PINK)

            if(cell.gandalfHere):
                self.SCREEN.blit(GANDALF, point)
            elif(cell.castleHere):
                self.SCREEN.blit(CASTLE, point)
            elif(cell.enemyHere):
                self.SCREEN.blit(ENEMY, point)
        pygame.display.update()    

    def delay(self, time):
        pygame.time.delay(time)
        
    def drawPath(self, path):
        counter = len(path) - 1
        for stage in path:
            self.table[stage].inPath = True
            self.table[stage].stage = counter
            counter -= 1
        self.draw()

    def printIndices(self):
        for cell in self.table:
            getEvent()
            pygame.draw.rect(self.SCREEN, WHITE, cell.rect, 1)
            cell.printIndex()


    def emptyCell(self, index):
        if (self.table[index].gandalfHere == False and self.table[index].castleHere == False and self.table[index].enemyHere == False):
            return True
        return False

    def placePieces(self):
        currentIndex = 0
        gandalfPlaced, castlePlaced = [False, False]
        print("Place the pieces\nPress g to place Gandalf\nPress c to place castle\nPress e to place enemies\nPress f if you finished")
        global DELAY_TIME
        DELAY_TIME = 100
        self.draw()
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_f):
                        if(castlePlaced == True and gandalfPlaced == True):
                            DELAY_TIME = 700
                            self.table[currentIndex].placing = False
                            self.draw()
                            return
                        else:
                            print("Gandalf or the castle have not been placed yet!!")

                    if(event.key == pygame.K_g and gandalfPlaced == False and self.emptyCell(currentIndex)):
                        self.table[currentIndex].gandalfHere = True
                        self.table[currentIndex].gandalfInitPlace = True 
                        gandalfPlaced = True

                    elif(event.key == pygame.K_c and castlePlaced == False and self.emptyCell(currentIndex)):
                        self.table[currentIndex].castleHere = True
                        castlePlaced = True

                    elif(event.key == pygame.K_e and self.emptyCell(currentIndex)):
                        self.table[currentIndex].enemyHere = True

                    if (event.key == pygame.K_LEFT and self.table[currentIndex].center[0] > 0):
                        self.table[currentIndex].placing = False
                        currentIndex -= int(self.HEIGHT / PIC_SIZE_X)
                        
                    elif (event.key == pygame.K_RIGHT and self.table[currentIndex].center[0] < self.WIDTH / PIC_SIZE_Y - 1):
                        self.table[currentIndex].placing = False
                        currentIndex += int(self.HEIGHT / PIC_SIZE_X)
                        
                    elif (event.key == pygame.K_UP) and (self.table[currentIndex].center[1] > 0):
                        self.table[currentIndex].placing = False
                        currentIndex -= 1
                        
                    elif (event.key == pygame.K_DOWN) and (self.table[currentIndex].center[1] < self.HEIGHT / PIC_SIZE_X - 1):
                        self.table[currentIndex].placing = False
                        currentIndex += 1
                    
                    self.table[currentIndex].placing = True
                    self.draw()
