import UI
from BFS import BFS 
from DFS import DFS 
from IDS import IDS
from Astar import Astar 
import math

class Total:
    def __init__(self):
        self.numOfRows, self.numOfCols = 5, 5
        self.UI = UI.Screen(self.numOfCols, self.numOfRows)
        self.table = self.UI.initField()

    def getInput(self):
        self.UI.placePieces()
        algorithmToRun = input("Enter algorithm to run: ")
        if algorithmToRun == "BFS":
            self.UX = BFS(self.table, self.numOfCols, self.numOfRows)
        elif algorithmToRun == "DFS":
            self.UX = DFS(self.table, self.numOfCols, self.numOfRows)
        elif algorithmToRun == "IDS":
            maxDepth = input("Enter max depth of IDS: ")
            self.UX = IDS(self.table, self.numOfCols, self.numOfRows, int(maxDepth))
        elif algorithmToRun == "A*":
            self.UX = Astar(self.table, self.numOfCols, self.numOfRows)
        self.PLACES_DONE = True

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            if(self.PLACES_DONE == False):
                self.getInput()
            found = self.UX.run()
            if found == -1:
                print("Loose!!!!")
                self.UI.draw()
                self.UI.delay(20000)
                self.UI.quit()     
                break
            elif found == -2:
                path = self.UX.getPath()
                # self.UX.clearFrontier()
                self.UX.clearExplored()
                self.UI.drawPath(path)
                self.UI.delay(20000)
                self.UI.quit()     
                break
            self.UI.draw()
            self.table[found].gandalfHere = False
            
            

total = Total()
total.flow()