
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
        self.startIndex, self.goalIndex = self.findStartAndEndPositions(table)
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
    
    def findStartAndEndPositions(self, table):
        startPosition = -1
        goalPosition = -1
        for cell in table:
            if cell.state == 'gi':
                startPosition = cell.index
            elif cell.state == 'c':
                goalPosition = cell.index
        return startPosition, goalPosition
    
    def goalTest(self, state):
        if state.position == self.goalState.position:
            print("Found!!!!")
            return 1
        else:
            return None
        
    def makeNewChild(self, state, offset, cost = 0):
        return State(state.position + offset, cost)
        # return node + offset

    def addToFrontier(self, child, state):
        # child = self.makeNewChild(state, offset)
        if ((not (child.position, child.cost) in self.frontier) and (not (child.position, child.cost) in self.explored)):  
            self.frontier.append((child.position, child.cost))
            self.parent[child.position] = state.position
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
        if (node - 1 >= 0 and self.table[node].Center[1] > 0 and self.table[node - 1].state != 'e'):
            return True
        return False

    def checkRight(self, node):
        # print("center: " + str(self.table[node].Center[0]))
        if(node + self.numberOfRows < self.numberOfCells and self.table[node].Center[0] < self.numberOfCols - 1 and self.table[node + self.numberOfRows].state != 'e'):
            return True
        return False

    def checkDown(self, node):
        if(node + 1 < self.numberOfCells and self.table[node].Center[1] < self.numberOfRows - 1 and self.table[node + 1].state != 'e'):
            return True
        return False

    def checkLeft(self, node):
        if(node - self.numberOfRows >= 0 and self.table[node].Center[0] > 0 and self.table[node - self.numberOfRows].state != 'e'):
            return True
        return False
