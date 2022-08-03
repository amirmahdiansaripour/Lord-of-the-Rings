import time
class Logic:
    def __init__(self, table, width, height):
        self.numberOfCells = len(table)
        self.numberOfCols = width
        self.numberOfRows = height
        self.startIndex, self.goalIndex, self.numOfAllies = self.findStartAndEndPositions(table)
        self.startState = (self.startIndex, 0)
        self.goalState = (self.goalIndex, self.numOfAllies)
        self.frontier = list()
        self.explored = dict()
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
            # print(str(node[1]) + str(self.goalState[1]))
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
            # print("hi")
            # print((node[0] + offset, node[1] + 1))
            return (node[0] + offset, node[1] + 1)
        else:
            return (node[0] + offset, node[1])
    

    def addToFrontier(self, node, state, offset):
        child = self.makeNewChild(node, state, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.frontier.append(child)
            
    
        


class BFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)

    def run(self, table):
        node = self.frontier.pop(0)
        self.explored[node] = True

        table[node[0]].gandalfHere = True
        matchResult = self.goalTest(node, table)
        if matchResult == 1:
            return -2
        elif matchResult == -1:
            return -1
        # UP
        if (table[node[0]].Center[1] > 0 and table[node[0] - 1].state != 'e'):
            self.addToFrontier(node, table[node[0] - 1].state, -1)
            # print("U")
        # RIGHT
        if(table[node[0]].Center[0] < self.numberOfCols - 1 and table[node[0] + 10].state != 'e'):
            self.addToFrontier(node, table[node[0] + 10].state, 10)           
            # print("R")     
        # DOWN
        if(table[node[0]].Center[1] < self.numberOfRows - 1 and table[node[0] + 1].state != 'e'):
            self.addToFrontier(node, table[node[0] + 1].state, 1)                
            # print("D")
        # LEFT
        if(table[node[0]].Center[0] > 0 and table[node[0] - 10].state != 'e'):
            self.addToFrontier(node, table[node[0] - 10].state, -10)                                
            # print("L")
        return node[0]
            