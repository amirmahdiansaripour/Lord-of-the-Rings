class Logic:
    def __init__(self, table, width, height):
        self.numberOfCells = len(table)
        self.numberOfCols = width
        self.numberOfRows = height
        self.startIndex, self.goalIndex, self.numOfAllies = self.findStartAndEndPositions(table)
        self.startState = (self.startIndex, 0)
        self.goalState = (self.goalIndex, self.numOfAllies)
        self.frontier = list()
        self.explored = list()
        self.parent = dict()
        

    def findStartAndEndPositions(self, table):
        startPosition = 0
        goalPosition = 0
        numOfAllies = 0
        for cell in table:
            if cell.state == 'gi':
                startPosition = cell.index
            elif cell.state == 'c':
                goalPosition = cell.index
            elif cell.state == 'a':
                numOfAllies += 1
        return startPosition, goalPosition, numOfAllies
    
    def goalTest(self, node, table):
        if node[0] == self.goalState[0]:
            if node[1] >= self.goalState[1]:
                print("Find!!!!")
                return 1
        elif table[node[0]].state == 'e':
            print("Loose!!!!")
            return -1
        else:
            return 0

    def makeNewChild(self, node, char, offset):
        if(char == 'a' and node[1] < self.numOfAllies):
            return (node[0] + offset, node[1] + 1)
        else:
            return (node[0] + offset, node[1])
    

    def addToFrontier(self, node, state, offset):
        child = self.makeNewChild(node, state, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.frontier.append(child)
            return True
        return False
            
    
        


class BFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)

    def run(self, table):
        if len(self.frontier) == 0:
            print("Loose!!!!")
            return -1
        node = self.frontier.pop(0)
        table[node[0]].inFrontier = False
        table[node[0]].gandalfHere = True
        table[node[0]].inExplored = True
        self.explored.append(node)
        matchResult = self.goalTest(node, table)
        if matchResult == 1:
            return -2
        elif matchResult == -1:
            return -1
        # UP
        if (table[node[0]].Center[1] > 0 and node[0] - 1 >= 0 and table[node[0] - 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, table[node[0] - 1].state, -1)
            if addedToFrontier:
                table[node[0] - 1].inFrontier = True
        # RIGHT
        if(table[node[0]].Center[0] < self.numberOfCols - 1 and node[0] + self.numberOfRows < self.numberOfCells and table[node[0] + self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, table[node[0] + self.numberOfRows].state, self.numberOfRows)           
            if addedToFrontier:
                table[node[0] + self.numberOfRows].inFrontier = True
        # DOWN
        if(table[node[0]].Center[1] < self.numberOfRows - 1 and node[0] + 1 < self.numberOfCells and table[node[0] + 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, table[node[0] + 1].state, 1)                
            if addedToFrontier:
                table[node[0] + 1].inFrontier = True
        # LEFT
        if(table[node[0]].Center[0] > 0 and node[0] - self.numberOfRows >= 0 and table[node[0] - self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, table[node[0] - self.numberOfRows].state, -self.numberOfRows)                                
            if addedToFrontier:
                table[node[0] - self.numberOfRows].inFrontier = True
        return node[0]
            