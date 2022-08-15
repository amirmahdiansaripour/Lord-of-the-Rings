
from tokenize import Triple

class State:
    def __init__(self, index, cost_ = 0):
        self.position = index
        self.cost = cost_


class Logic:
    def __init__(self, table, width, height):
        self.table = table
        self.numberOfCells = len(table)
        self.numberOfCols = width
        self.numberOfRows = height
        self.startIndex, self.goalIndex = self.findStartAndEndPositions()
        self.startState = State(self.startIndex)
        self.goalState = State(self.goalIndex)
        self.frontier = list()
        self.explored = list()
        self.parent = dict()
        self.parent[self.startState.position] = -1
        
    def clearFrontier(self):
        for cell in self.table:
            cell.inFrontier = False

    def clearExplored(self):
        for cell in self.table:
            cell.inExplored = False    
    
    def findStartAndEndPositions(self):
        startPosition = -1
        goalPosition = -1
        for cell in self.table:
            if cell.gandalfInitPlace:
                startPosition = cell.index
            elif cell.castleHere:
                goalPosition = cell.index
        return startPosition, goalPosition
    
    def preprocessNode(self, node):
        position = node.position
        self.table[position].inFrontier = False
        self.table[position].gandalfHere = True
        self.table[position].inExplored = True
        self.explored.append((node.position, node.cost))
        return self.goalTest(node)

    def goalTest(self, state):
        if state.position == self.goalState.position:
            print("Found!!!!")
            return 1
        else:
            return None
        
    def makeNewChild(self, parent, offset, cost = 0):
        return State(parent.position + offset, cost)
        # return node + offset

    def checkFrontierandExplore(self, child, parent):
        # child = self.makeNewChild(state, offset)
        if (self.table[child.position].inFrontier == False) and (self.table[child.position].inExplored == False):
            self.parent[child.position] = parent.position
            return True
        return False
            
    def findPath(self, pathList, index):
        # print("index: " + str(index))
        if self.parent.get(index) == -1:
            return pathList
        pathList.append(self.parent.get(index))
        return self.findPath(pathList, self.parent.get(index))
    
    def getPath(self):
        return self.findPath([], self.goalState.position)
        
    def checkUP(self, node):
        if (node - 1 >= 0 and self.table[node].center[1] > 0 and self.table[node - 1].enemyHere == False and self.table[node - 1].dontEnter == False):
            return True
        return False

    def checkRight(self, node):
        # print("center: " + str(self.table[node].center[0]))
        if(node + self.numberOfRows < self.numberOfCells and self.table[node].center[0] < self.numberOfCols - 1 and self.table[node + self.numberOfRows].enemyHere == False and self.table[node + self.numberOfRows].dontEnter == False):
            return True
        return False

    def checkDown(self, node):
        if(node + 1 < self.numberOfCells and self.table[node].center[1] < self.numberOfRows - 1 and self.table[node + 1].enemyHere == False and self.table[node + 1].dontEnter == False):
            return True
        return False

    def checkLeft(self, node):
        if(node - self.numberOfRows >= 0 and self.table[node].center[0] > 0 and self.table[node - self.numberOfRows].enemyHere == False and self.table[node - self.numberOfRows].dontEnter == False):
            return True
        return False
