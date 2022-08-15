from BFS import BFS
from _heapq import heappush, heappop
from UX import State
import math

class Astar(BFS):
    def __init__(self, table, width, height, alpha = 1):
        super().__init__(table, width, height)
        self.alpha = int(alpha)
        self.frontier = []
        heappush(self.frontier, (0 + self.hueristic(self.startIndex), self.startIndex))

    def hueristic(self, position):
        currX = int(self.table[position].x)
        currY = int(self.table[position].y)
        goalX = int(self.table[self.goalIndex].x)
        goalY = int(self.table[self.goalIndex].y)
        squaredDistance = (currX - goalX)**2 + (currY - goalY)**2
        return self.alpha * math.sqrt(squaredDistance)

    def pop(self):
        poppedNode = heappop(self.frontier)
        # print(poppedNode)
        poppedNode = State(poppedNode[1], poppedNode[0])
        return poppedNode
    
    def calcCostofNewState(self, parent, offset):
        realCost = parent.cost - self.hueristic(parent.position)
        realCost += 1
        totalCost = realCost + self.hueristic(parent.position + offset)
        return totalCost

    def makeNewChild(self, parent, offset):
        return State(parent.position + offset, self.calcCostofNewState(parent, offset))

    def push(self, node):
        heappush(self.frontier, (node.cost, node.position))
        