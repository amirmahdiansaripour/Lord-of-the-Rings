from ast import Return
import copy

class Logic:
    def __init__(self, table):
        self.numberOfCells = len(table)
        self.startIndex, self.goalIndex, self.numOfAllies = self.findStartAndEndPositions(table)
        self.startState = (self.startIndex, 0)
        self.goalState = (self.goalIndex, self.numOfAllies)

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
    
    def makeNewChild(self, node, char):
        if char == 'a':
            return (node[0] - 1, node[1] + 1)
        else:
            return (node[0] - 1, node[1])



class BFS(Logic):
    def __init__(self, table):
        super().__init__(table)
        self.parent = dict()
        self.frontier = list()
        self.explored = dict()
        self.parent[self.startState] = -1
        self.frontier.append(self.startState)

    def run(self, table):
        if(len(self.frontier) == 0):
            print("Goal does not exist!")
            return

        else:
            node = self.frontier.pop(0)
            # print(node[0])
            self.explored[node] = True
            if node == self.goalState:
                print("found!!!!!!!!!")
                return
            child = copy.deepcopy(node)

            if (node[0] - 1 in range(0, self.numberOfCells) and table[node[0] - 1].state != 'e'):
                child = self.makeNewChild(child, table[node[0]].state)
                # table[node[0]].state = 'o'
                table[node[0] - 1].state = 'g'
                self.frontier.append(child)
        return
                