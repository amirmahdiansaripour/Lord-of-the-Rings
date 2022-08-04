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
        


class BFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)

    def run(self, table):
        if len(self.frontier) == 0:
            print("Loose!!!!")
            return -1
        node = self.frontier.pop(0)
        table[node].inFrontier = False
        table[node].gandalfHere = True
        table[node].inExplored = True
        self.explored.append(node)
        matchResult = self.goalTest(node)
        if matchResult == 1:
            return -2
        elif matchResult == -1:
            return -1
        # UP
        if (table[node].Center[1] > 0 and node - 1 >= 0 and table[node - 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -1)
            if addedToFrontier:
                table[node - 1].inFrontier = True
        # RIGHT
        if(table[node].Center[0] < self.numberOfCols - 1 and node + self.numberOfRows < self.numberOfCells and table[node + self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, self.numberOfRows)           
            if addedToFrontier:
                table[node + self.numberOfRows].inFrontier = True
        # DOWN
        if(table[node].Center[1] < self.numberOfRows - 1 and node + 1 < self.numberOfCells and table[node + 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, 1)                
            if addedToFrontier:
                table[node + 1].inFrontier = True
        # LEFT
        if(table[node].Center[0] > 0 and node - self.numberOfRows >= 0 and table[node - self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -self.numberOfRows)                                
            if addedToFrontier:
                table[node - self.numberOfRows].inFrontier = True
        return node
            