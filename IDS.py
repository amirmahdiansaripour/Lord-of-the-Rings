from tkinter.tix import Tree
from DFS import DFS
from UX import Logic

class IDS(Logic):
    def __init__(self, table, width, height, maxDepth):
        super().__init__(table, width, height)
        self.maxDepth = maxDepth
        self.currentDepth = 1
        self.makeBorderSet()
        self.DFS = DFS(self.table, self.numberOfCols, self.numberOfRows)
        
    def calcManhattanDist(self, node):
        return abs(node.center[0] - self.table[self.startIndex].center[0]) + abs(node.center[1] - self.table[self.startIndex].center[1])

    def makeBorderSet(self):
        for cell in self.table:
            distance = self.calcManhattanDist(cell)
            if distance >= self.currentDepth + 1:
                cell.dontEnter = True
            if distance == self.currentDepth + 1:
                cell.label = str(self.currentDepth + 1)
                cell.inBorder = True

    def clearBoard(self):
        for cell in self.table:
            [cell.inFrontier, cell.inExplored, cell.inBorder, cell.dontEnter] = [False, False, False, False]

    def run(self):
        found = self.DFS.run()
        if found == -1:
            if self.currentDepth >= self.maxDepth:
                return -1
            self.currentDepth += 1
            self.clearBoard()
            self.makeBorderSet()
            self.DFS = DFS(self.table, self.numberOfCols, self.numberOfRows)
            self.parent.clear()
            self.parent = self.DFS.parent
            return self.startIndex
        return found
