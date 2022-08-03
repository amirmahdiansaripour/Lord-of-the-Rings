import UI
import UX

class Total:
    def __init__(self):
        numOfRows, numOfCols = 10, 15
        self.UI = UI.Screen(numOfCols, numOfRows)
        self.table = self.UI.initField()

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            if(self.PLACES_DONE == False):
                self.UI.placePeices(self.table)
                self.UX = UX.BFS(self.table)
                self.PLACES_DONE = True
            found = self.UX.run(self.table)
            if found == -1 or found == -2: 
                break
            self.UI.draw(self.table)
            self.table[found].gandalfHere = False
            

total = Total()
total.flow()