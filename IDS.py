from DFS import DFS
from UX import Logic

class IDS(Logic):
    def __init__(self, table, width, height, maxDepth):
        super().__init__(table, width, height)
        self.maxDepth = maxDepth
        self.currentDepth = 1
        self.DFS = DFS(self.table, self.numberOfCols, self.numberOfRows)


    def makeBorderSet(self):
        upBound = self.startIndex - self.maxDepth
        upLimit = upBound - 1 if upBound - 1 >= 0 and self.table[upBound].Center[1] > 0 else 0
        
        downBound = self.startIndex + self.maxDepth
        downLimit = downBound + 1 if downBound + 1 < self.numberOfCells and self.table[downBound].Center[1] < self.numberOfRows - 1 else self.numberOfRows - 1
        
        rightBound = self.startIndex + ((self.maxDepth + 1) * self.numberOfRows)
        rightLimit = rightBound if rightBound < self.numberOfCells and self.table[rightBound - self.numberOfRows].Center[0] < self.numberOfCols - 1 else self.numberOfCols - 1

        leftBound = self.startIndex - ((self.maxDepth + 1) * self.numberOfRows)
        leftLimit = leftBound if leftBound >= 0 and self.table[rightBound + self.numberOfRows].Center[0] > 0 else 0

        self.table[leftLimit].inBorder = True
        self.table[rightLimit].inBorder = True
        self.table[upLimit].inBorder = True
        self.table[downLimit].inBorder = True
        input("HI")


    def run(self):
        self.makeBorderSet()