from turtle import pos
from UX import Logic
from UX import State

class DFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.frontier.append(self.startState)
        self.nodeToExplore = self.startState

    def action(self, position, offset):
            child = self.makeNewChild(self.nodeToExplore, offset)
            addedToFrontier = self.addToFrontier(child, self.nodeToExplore)
            if addedToFrontier:
                self.frontier.append((child.position, child.cost))
                self.table[position + offset].inFrontier = True
                self.nodeToExplore = child
                return True
            else:
                return False 


    def DFSRun(self):
        position = self.nodeToExplore.position
        matchResult = self.preprocessNode(self.nodeToExplore)
        if matchResult == 1:
            self.table[self.nodeToExplore.position].gandalfHere = True 
            return -2

        if (self.checkUP(position)):
            nextPossible = self.action(position, -1)
            if(nextPossible):
                return position
        
        if(self.checkRight(position)):
            nextPossible = self.action(position, self.numberOfRows)
            if(nextPossible):
                return position    

        if(self.checkDown(position)):
            nextPossible = self.action(position, 1)        
            if(nextPossible):
                return position

        if(self.checkLeft(position)):
            nextPossible = self.action(position, -self.numberOfRows)
            if(nextPossible):
                return position
        return -1
        

    def findAnotherWay(self, node):
        if(node == -1):
            return -1
        if (self.checkUP(node) and self.table[node - 1].inExplored == False):
            self.parent[node - 1] = node
            return self.makeNewChild(State(node), -1)

        if(self.checkRight(node) and self.table[node + self.numberOfRows].inExplored == False):
            self.parent[node + self.numberOfRows] = node
            return self.makeNewChild(State(node), self.numberOfRows)

        if(self.checkDown(node) and self.table[node + 1].inExplored == False):
            self.parent[node + 1] = node
            return self.makeNewChild(State(node), 1)

        if(self.checkLeft(node) and self.table[node - self.numberOfRows].inExplored == False):
            self.parent[node - self.numberOfRows] = node
            return self.makeNewChild(State(node), -self.numberOfRows)
        
        return self.findAnotherWay(self.parent[node])

    def getLatestExploredNode(self):
        return self.nodeToExplore.position

    def run(self):
        nextStep = self.DFSRun()
        if nextStep == -1:
            self.table[self.nodeToExplore.position].gandalfHere = False
            anotherWay = self.findAnotherWay(self.nodeToExplore.position) 
            if anotherWay == -1:
                return -1    
            self.nodeToExplore = anotherWay
            return anotherWay.position
        return nextStep