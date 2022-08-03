import UI

class Total:
    def __init__(self):
        # numOfRows, numOfCols = input("Enter number of rows and columns: ").split()
        numOfRows, numOfCols = 10, 15
        self.UI = UI.Screen(numOfCols, numOfRows)
    
    def flow(self):
        self.PLACES_DONE = False
        self.UI.initField()

        while(True):
            self.UI.draw()
            if(self.PLACES_DONE == False):
                self.UI.placePeices()
                self.PLACES_DONE = True



total = Total()
total.flow()