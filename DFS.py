from turtle import pos
from UX import Logic
from UX import State
import math

class DFS(Logic):
    def __init__(self, table, width, height, maxDepth = math.inf):
        super().__init__(table, width, height)
        self.frontier.append(self.startState)
        self.nodeToExplore = self.startState
        self.maxDepth = maxDepth
        self.currentDepth = 0


    def handleRepeatedStates(self, index, offset):
        parent = self.table[index]
        child = self.table[index + offset] 
        if(child.inExplored == False and child.enemyHere == False):
            self.table[index + offset].cost = parent.cost + 1
            return True
        elif (child.inExplored == True and child.enemyHere == False and parent.cost + 1 < child.cost):
            self.table[index + offset].cost = parent.cost + 1
            return True
        return False

    def action(self, position, offset):
            addedToFrontier = self.handleRepeatedStates(position, offset)
            if addedToFrontier:
                self.parent[position + offset] = self.nodeToExplore.position
                child = self.makeNewChild(self.nodeToExplore, offset, self.table[position].cost + 1)
                # self.table[self.nodeToExplore.position + offset].cost = self.table[self.nodeToExplore.position].cost + 1
                self.frontier.append((child.position, child.cost))
                self.nodeToExplore = child
                return True
            else:
                return False 


    def DFSRun(self):
        position = self.nodeToExplore.position
        matchResult = self.preprocessNode(self.nodeToExplore)
        self.currentDepth += 1
        if matchResult == 1:
            self.table[self.nodeToExplore.position].gandalfHere = True 
            return -2
        
        if self.currentDepth == self.maxDepth:
            return -1
        
        # print("cur depth: " + str(self.currentDepth))

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
        if(node == -1 or self.currentDepth < 0):
            return -1
        self.currentDepth -= 1
        # print("Node: " + str(node))
        if (self.checkUP(node) and self.handleRepeatedStates(node, -1)):
            self.parent[node - 1] = node
            return self.makeNewChild(State(node), -1, self.table[node].cost + 1)

        if(self.checkRight(node) and self.handleRepeatedStates(node, self.numberOfRows)):
            self.parent[node + self.numberOfRows] = node
            return self.makeNewChild(State(node), self.numberOfRows, self.table[node].cost + 1)

        if(self.checkDown(node) and self.handleRepeatedStates(node, 1)):
            self.parent[node + 1] = node
            return self.makeNewChild(State(node), 1, self.table[node].cost + 1)

        if(self.checkLeft(node) and self.handleRepeatedStates(node, -self.numberOfRows)):
            self.parent[node - self.numberOfRows] = node
            return self.makeNewChild(State(node), -self.numberOfRows, self.table[node].cost + 1)
        
        return self.findAnotherWay(self.parent[node])

    def getLatestExploredNode(self):
        return self.nodeToExplore.position

    def run(self):
        nextStep = self.DFSRun()
        if nextStep == -1:
            self.table[self.nodeToExplore.position].gandalfHere = False
            # print("Just explored node: " + str(self.nodeToExplore.position))
            self.table[self.nodeToExplore.position].cost = self.table[self.parent[self.nodeToExplore.position]].cost + 1
            pos = self.nodeToExplore.position
            anotherWay = self.findAnotherWay(self.parent[self.nodeToExplore.position]) 
            self.table[pos].gandalfHere = True
            self.table[pos].label = str(self.table[pos].cost - 1)
            if anotherWay == -1:
                return -1    
            self.nodeToExplore = anotherWay
            return pos
        if (nextStep != -1 and nextStep != -2):
            self.table[nextStep].cost = self.table[self.parent[nextStep]].cost + 1
            self.table[nextStep].label = str(self.table[nextStep].cost - 1)
        return nextStep