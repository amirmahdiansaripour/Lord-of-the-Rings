
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
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)

        
    def findStartAndEndPositions(self, table):
        startPosition = 0
        goalPosition = 0
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
            return 0

    def makeNewChild(self, state, offset):
        return State(state.position + offset, state.cost + 1)
        # return node + offset

    def addToFrontier(self, child, state, offset):
        # child = self.makeNewChild(state, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.frontier.append(child)
            self.parent[child.position] = state
            return True
        return False
            
    def findPath(self, pathList, index):
        if self.parent.get(index) == -1:
            return pathList
        pathList.append(self.parent.get(index))
        return self.findPath(pathList, self.parent.get(index))
    
    def getPath(self):
        # print(self.goalState)
        # print(self.parent)
        return self.findPath([], self.goalState.position)
        
    def checkUP(self, node):
        if (self.table[node].Center[1] > 0 and node - 1 >= 0 and self.table[node - 1].state != 'e'):
            return True
        return False

    def checkRight(self, node, table):
        if(table[node].Center[0] < self.numberOfCols - 1 and node + self.numberOfRows < self.numberOfCells and table[node + self.numberOfRows].state != 'e'):
            return True
        return False

    def checkDown(self, node, table):
        if(table[node].Center[1] < self.numberOfRows - 1 and node + 1 < self.numberOfCells and table[node + 1].state != 'e'):
            return True
        return False

    def checkLeft(self, node, table):
        if(table[node].Center[0] > 0 and node - self.numberOfRows >= 0 and table[node - self.numberOfRows].state != 'e'):
            return True
        return False
