from turtle import pos
from UX import Logic
from UX import State

class DFS(Logic):
    def __init__(self, table, width, height, maxDepth):
        super().__init__(table, width, height)
        self.frontier.append(self.startState)
        self.nodeToExplore = self.startState
        self.maxDepth = maxDepth
        self.currentDepth = 0

    def action(self, position, offset):
            child = self.makeNewChild(self.nodeToExplore, offset)
            addedToFrontier = self.addToFrontier(child, self.nodeToExplore)
            if addedToFrontier:
                self.table[position + offset].inFrontier = True
                self.nodeToExplore = child
                return position
            else:
                return None 


    def DFSRun(self):
        if self.currentDepth == self.maxDepth:
            return -1
        self.currentDepth += 1
        
        position = self.nodeToExplore.position
        self.table[position].inFrontier = False
        self.table[position].inExplored = True
        self.table[position].gandalfHere = True
        self.explored.append((self.nodeToExplore.position, self.nodeToExplore.cost))
        matchResult = self.goalTest(self.nodeToExplore)
        
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
        

    def findAnotherWay(self, node, latestStage):
        if(node == -1):
            return -1
        if (self.checkUP(node) and self.table[node - 1].inExplored == False):
            self.parent[node - 1] = latestStage
            return self.makeNewChild(State(node), -1)

        if(self.checkRight(node) and self.table[node + self.numberOfRows].inExplored == False):
            self.parent[node + self.numberOfRows] = latestStage
            return self.makeNewChild(State(node), self.numberOfRows)

        if(self.checkDown(node) and self.table[node + 1].inExplored == False):
            self.parent[node + 1] = latestStage
            return self.makeNewChild(State(node), 1)

        if(self.checkLeft(node) and self.table[node - self.numberOfRows].inExplored == False):
            self.parent[node - self.numberOfRows] = latestStage
            return self.makeNewChild(State(node), -self.numberOfRows)
        
        return self.findAnotherWay(self.parent[node], latestStage)

    def run(self):
        nextStep = self.DFSRun()
        if nextStep == -1:
            self.table[self.nodeToExplore.position].gandalfHere = False
            anotherWay = self.findAnotherWay(self.nodeToExplore.position, self.nodeToExplore.position) 
            if anotherWay == -1:
                print("Loose !!!!")
                return -1    
            self.nodeToExplore = anotherWay
            return anotherWay.position
        return nextStep