from tkinter.tix import Tree
from DFS import DFS
from UX import Logic

class IDS(Logic):
    def __init__(self, table, width, height, maxDepth):
        super().__init__(table, width, height)
        self.maxDepth = maxDepth
        self.currentDepth = 1
        # self.makeBorderSet()
        self.newDFS = False
        self.DFS = DFS(self.table, self.numberOfCols, self.numberOfRows, self.currentDepth)
        
    
    def clearBoard(self):
        # print("Entered clear board func\n")
        for cell in self.table:
            [cell.inFrontier, cell.inExplored] = [False, False]

    def makeNewDFS(self):
        self.currentDepth += 1
        self.clearBoard()
        # self.makeBorderSet()
        self.DFS = DFS(self.table, self.numberOfCols, self.numberOfRows, self.currentDepth)
        self.parent.clear()
        self.parent = self.DFS.parent
        self.newDFS = False

    def run(self):
        if self.newDFS:
            self.makeNewDFS()
        found = self.DFS.run()
        if found == -1:
            if self.currentDepth > self.maxDepth:
                return -1
            latestNode = self.DFS.getLatestExploredNode()
            self.table[latestNode].inExplored = True
            self.newDFS = True
            return latestNode
        return found
