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
        

    def anotherChild(self, node, latestStage):
        if(node == -1):
            return -1
        if (self.checkUP(node)):
            if(self.table[node - 1].inExplored == False):
                self.parent[node - 1] = latestStage
                return self.makeNewChild(State(node), -1)

        if(self.checkRight(node)):
            if(self.table[node + self.numberOfRows].inExplored == False):
                self.parent[node + self.numberOfRows] = latestStage
                return self.makeNewChild(State(node), self.numberOfRows)

        if(self.checkDown(node)):
            if(self.table[node + 1].inExplored == False):
                self.parent[node + 1] = latestStage
                return self.makeNewChild(State(node), 1)

        if(self.checkLeft(node)):
            if(self.table[node - self.numberOfRows].inExplored == False):
                self.parent[node - self.numberOfRows] = latestStage
                return self.makeNewChild(State(node), -self.numberOfRows)
        
        return self.anotherChild(self.parent[node], latestStage)

    def run(self):
        res = self.DFSRun(self.nodeToExplore)
        if res == -1:
            anotherWay = self.anotherChild(self.nodeToExplore.position, self.nodeToExplore.position) 
            if anotherWay == -1:
                print("Loose !!!!")
                return -1    
            self.table[self.nodeToExplore.position].gandalfHere = False
            self.nodeToExplore = anotherWay
            return self.nodeToExplore.position
        return res