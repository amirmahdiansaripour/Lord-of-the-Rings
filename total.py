import UI
import UX
import time
class Total:
    def __init__(self):
        self.numOfRows, self.numOfCols = 10, 15
        self.UI = UI.Screen(self.numOfCols, self.numOfRows)
        self.table = self.UI.initField()

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            if(self.PLACES_DONE == False):
                self.UI.placePeices(self.table)
                self.UX = UX.BFS(self.table, self.numOfCols, self.numOfRows)
                self.PLACES_DONE = True
            found = self.UX.run(self.table)
            if found == -1 or found == -2:
                self.UI.draw(self.table)
                time.sleep(4)     
                break
            self.UI.draw(self.table)
            self.table[found].gandalfHere = False
            

total = Total()
total.flow()