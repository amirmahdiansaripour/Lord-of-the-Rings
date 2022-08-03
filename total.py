import UI

class Total:
    def __init__(self):
        numOfRows, numOfCols = 10, 15
        self.UI = UI.Screen(numOfCols, numOfRows)
        self.table = self.UI.initField()

    def flow(self):        
        self.PLACES_DONE = False
        while(True):
            self.UI.draw(self.table)
            if(self.PLACES_DONE == False):
                self.UI.placePeices(self.table)
                self.PLACES_DONE = True

total = Total()
total.flow()