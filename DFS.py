from turtle import pos
from UX import Logic

class DFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.nodeToExplore = self.startState


    def action(self, position, offset):
            child = self.makeNewChild(self.nodeToExplore, offset)
            addedToFrontier = self.addToFrontier(child, self.nodeToExplore, offset)
            if addedToFrontier:
                self.table[position + offset].inFrontier = True
                self.nodeToExplore = child
                return position


    def DFSRun(self, node):
        position = node.position
        self.table[position].inFrontier = False
        self.table[position].inExplored = True
        self.table[position].gandalfHere = True
        self.explored.append(node)
        matchResult = self.goalTest(node)
        
        if matchResult == 1:
            self.table[self.nodeToExplore].gandalfHere = True 
            return -2

        if (self.checkUP(position)):
            return self.action(position, -1)
        
        if(self.checkRight(position)):
            return self.action(position, self.numberOfRows)

        if(self.checkDown(position)):
            return self.action(position, 1)        
        
        if(self.checkLeft(position)):
            return self.action(position, -self.numberOfRows)

        return -1

    def allNodesExpanded(self, table):
        for cell in table:
            if cell.inExplored == False:
                return False
        return True
        

    def anotherChild(self, table):
        if (self.checkUP(self.startState.position, table)):
            if(table[self.startState.position - 1].inExplored == False):
                return self.startState.position - 1

        if(self.checkRight(self.startState.position, table)):
            if(table[self.startState.position + self.numberOfRows].inExplored == False):
                return self.startState.position + self.numberOfRows

        if(self.checkLeft(self.startState.position, table)):
            if(table[self.startState.position - self.numberOfRows].inExplored == False):
                return self.startState.position - self.numberOfRows
        
        if(self.checkDown(self.startState.position, table)):
            if(table[self.startState.position + 1].inExplored == False):
                return self.startState.position + 1
        
        return -1

    def run(self):
        res = self.DFSRun(self.nodeToExplore)
        # if res == -1:
        #     anotherWay = self.anotherChild(table) 
        #     if  anotherWay == -1:
        #         print("Loose !!!!")
        #         return -1    
        #     table[self.nodeToExplore].gandalfHere = False
        #     self.parent[anotherWay] = self.nodeToExplore
        #     self.nodeToExplore = anotherWay
        #     return self.nodeToExplore
        return res