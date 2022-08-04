
class Logic:
    def __init__(self, table, width, height):
        self.numberOfCells = len(table)
        self.numberOfCols = width
        self.numberOfRows = height
        self.startState, self.goalState = self.findStartAndEndPositions(table)
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
    
    def goalTest(self, node):
        if node == self.goalState:
            print("Found!!!!")
            return 1
        else:
            return 0

    def makeNewChild(self, node, offset):
        return node + offset

    def addToFrontier(self, node, offset):
        child = self.makeNewChild(node, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.frontier.append(child)
            self.parent[child] = node
            return True
        return False
            
    def findPath(self, pathList, index):
        if self.parent.get(index) == -1:
            return pathList
        pathList.append(self.parent.get(index))
        return self.findPath(pathList, self.parent.get(index))
    
    def getPath(self):
        return self.findPath([], self.goalState)
        
