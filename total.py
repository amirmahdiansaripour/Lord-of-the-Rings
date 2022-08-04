import UI
import UX
class Total:
    def __init__(self):
        self.numOfRows, self.numOfCols = 10, 10
        self.UI = UI.Screen(self.numOfCols, self.numOfRows)
        self.table = self.UI.initField()

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            if(self.PLACES_DONE == False):
                self.UI.placePeices(self.table)
                algorithmToRun = input("Enter algorithm to run :")
                if algorithmToRun == "BFS":
                    self.UX = UX.BFS(self.table, self.numOfCols, self.numOfRows)
                self.PLACES_DONE = True
            found = self.UX.run(self.table)
            if found == -1:
                break
            elif found == -2:
                path = self.UX.getPath()
                self.UI.drawPath(self.table, path)
                self.UI.delay(8000)     
                break
            self.UI.draw(self.table)
            self.table[found].gandalfHere = False
            

total = Total()
total.flow()