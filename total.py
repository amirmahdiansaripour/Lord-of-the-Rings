import UI
from BFS import BFS 
from DFS import DFS 

class Total:
    def __init__(self):
        self.numOfRows, self.numOfCols = 10, 10
        self.UI = UI.Screen(self.numOfCols, self.numOfRows)
        self.table = self.UI.initField()

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            if(self.PLACES_DONE == False):
                self.UI.placePeices()
                algorithmToRun = input("Enter algorithm to run :")
                if algorithmToRun == "BFS":
                    self.UX = BFS(self.table, self.numOfCols, self.numOfRows)
                elif algorithmToRun == "DFS":
                    self.UX = DFS(self.table, self.numOfCols, self.numOfRows)
                self.PLACES_DONE = True
            found = self.UX.run()
            if found == -1:
                break
            elif found == -2:
                path = self.UX.getPath()
                self.UI.drawPath(path)
                self.UI.delay(8000)     
                break
            self.UI.draw()
            self.table[found].gandalfHere = False
            

total = Total()
total.flow()