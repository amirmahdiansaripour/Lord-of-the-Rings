from ast import Return
import copy

class Logic:
    def __init__(self, table):
        self.numberOfCells = len(table)
        self.startIndex, self.goalIndex, self.numOfAllies = self.findStartAndEndPositions(table)
        self.startState = (self.startIndex, 0)
        self.goalState = (self.goalIndex, self.numOfAllies)
        self.prevState = dict()
        self.frontier = list()
        self.explored = dict()
        self.parent = dict()
        

    def findStartAndEndPositions(self, table):
        startPosition = 0
        goalPosition = 0
        numOfAllies = 0
        for cell in table:
            if cell.state == 'g':
                startPosition = cell.index
            elif cell.state == 'c':
                goalPosition = cell.index
            elif cell.state == 'a':
                numOfAllies += 1
        return startPosition, goalPosition, numOfAllies
    
    def makeNewChild(self, node, char, offset):
        if char == 'a':
            return (node[0] + offset, node[1] + 1)
        else:
            return (node[0] + offset, node[1])
    
    def goalTest(self, node, table):
        if node == self.goalState:
            print("Find!!!!")
            return 1
        elif table[node[0]].state == 'e':
            print("Loose!!!!")
            return -1
        else:
            return 0

    def addToFrontier(self, state, index, offset):
        child = self.makeNewChild(child, state, offset)
        if ((not child in self.frontier) and (not child in self.explored)):  
            self.prevState[child] = (index, state) 
            self.frontier.append(child)
            
    
        


class BFS(Logic):
    def __init__(self, table):
        super().__init__(table)
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)
        self.prevState[self.startState] = (self.startIndex, 'o')

    def run(self, table):
        if(len(self.frontier) == 0):
            print("Goal does not exist!")
            return False

        else:
            node = self.frontier.pop(0)
            prevState = self.prevState.get(node)
            table[prevState[0]].state = prevState[1]
            self.explored[node] = True

            matchResult = self.goalTest(node, table)
            if matchResult == 1:
                return True
            elif matchResult == -1:
                return False
            
            child = copy.deepcopy(node)

            if (node[0] - 1 in range(0, self.numberOfCells) and table[node[0] - 1].state != 'e'):
                child = self.makeNewChild(child, table[node[0]].state, -1)
                self.prevState[child] = (node[0], table[node[0]].state) 
                self.frontier.append(child)
            
            # if(node[0] + 10 in range(0, self.numberOfCells) and table[node[0] + 10].state != 'e'):
            #     child = self.makeNewChild(child, table[node[0]].state, 10)
            #     self.prevState[child] = (node[0] - 1, table[node[0] - 1].state) 
            #     self.frontier.append(child)
            
            table[node[0]].state = 'g'
            
            
        return False
                