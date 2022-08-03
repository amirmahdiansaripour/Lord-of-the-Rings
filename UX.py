
class Logic:
    def __init__(self, table):
        self.numberOfCells = len(table)
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
            if  node[1] >= self.goalState[1]:
                print("Find!!!!")
                return 1
        elif table[node[0]].state == 'e':
            print("Loose!!!!")
            return -1
        else:
            return 0

    def makeNewChild(self, node, char, offset):
        if char == 'a':
            return (node[0] + offset, node[1] + 1)
        else:
            return (node[0] + offset, node[1])
    

    def addToFrontier(self, node, state, offset):
        child = self.makeNewChild(node, state, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.frontier.append(child)
            
    
        


class BFS(Logic):
    def __init__(self, table):
        super().__init__(table)
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)

    def run(self, table):
        if(len(self.frontier) == 0):
            print("Goal does not exist!")
            return -1

        else:
            node = self.frontier.pop(0)
            self.explored[node] = True

            matchResult = self.goalTest(node, table)
            if matchResult == 1:
                return -2
            elif matchResult == -1:
                return -1
            
            if (node[0] - 1 in range(0, self.numberOfCells) and table[node[0] - 1].state != 'e'):
                self.addToFrontier(node, table[node[0]].state, -1)

            if(node[0] + 1 in range(0, self.numberOfCells) and table[node[0] + 1].state != 'e'):
                self.addToFrontier(node, table[node[0]].state, 1)                

            if(node[0] + 10 in range(0, self.numberOfCells) and table[node[0] + 10].state != 'e'):
                self.addToFrontier(node, table[node[0]].state, 10)                

            if(node[0] - 10 in range(0, self.numberOfCells) and table[node[0] - 10].state != 'e'):
                self.addToFrontier(node, table[node[0]].state, -10)                                
            
            table[node[0]].gandalfHere = True
            return node[0]
                