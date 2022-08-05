from turtle import pos
from UX import Logic

class DFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.nodeToExplore = self.startState


    def action(self, position, offset):
            child = self.makeNewChild(self.nodeToExplore, offset)
            addedToFrontier = self.addToFrontier(child, self.nodeToExplore)
            if addedToFrontier:
                self.table[position + offset].inFrontier = True
                self.nodeToExplore = child
                return position
            else:
                return None 


    def DFSRun(self, node):
        position = node.position
        self.table[position].inFrontier = False
        self.table[position].inExplored = True
        self.table[position].gandalfHere = True
        self.explored.append((node.position, node.cost))
        matchResult = self.goalTest(node)
        
        if matchResult == 1:
            self.table[self.nodeToExplore.position].gandalfHere = True 
            return -2

        if (self.checkUP(position)):
            nextPossible = self.action(position, -1)
            if(nextPossible != None):
                return nextPossible
        
        if(self.checkRight(position)):
            nextPossible = self.action(position, self.numberOfRows)
            if(nextPossible != None):
                return nextPossible    

        if(self.checkDown(position)):
            nextPossible = self.action(position, 1)        
            if(nextPossible != None):
                return nextPossible

        if(self.checkLeft(position)):
            nextPossible = self.action(position, -self.numberOfRows)
            if(nextPossible != None):
                return nextPossible

        return -1

    def allNodesExpanded(self, table):
        for cell in table:
            if cell.inExplored == False:
                return False
        return True
        

    def anotherChild(self):
        if (self.checkUP(self.startState.position)):
            if(self.table[self.startState.position - 1].inExplored == False):
                return self.makeNewChild(self.startState, -1)

        if(self.checkRight(self.startState.position)):
            if(self.table[self.startState.position + self.numberOfRows].inExplored == False):
                return self.makeNewChild(self.startState, self.numberOfRows)

        if(self.checkDown(self.startState.position)):
            if(self.table[self.startState.position + 1].inExplored == False):
                return self.makeNewChild(self.startState, 1)

        if(self.checkLeft(self.startState.position)):
            if(self.table[self.startState.position - self.numberOfRows].inExplored == False):
                return self.makeNewChild(self.startState, -self.numberOfRows)
        
        return -1

    def run(self):
        res = self.DFSRun(self.nodeToExplore)
        if res == -1:
            anotherWay = self.anotherChild() 
            if  anotherWay == -1:
                print("Loose !!!!")
                return -1    
            self.table[self.nodeToExplore.position].gandalfHere = False
            self.parent[anotherWay.position] = self.nodeToExplore.position
            self.nodeToExplore = anotherWay
            return self.nodeToExplore.position
        return res