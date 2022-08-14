from BFS import BFS
from _heapq import heappush, heappop
import math

class Astar(BFS):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.initFrontier()

    def hueristic(self, index):
        currX = self.table[index].x
        currY = self.table[index].y
        goalX = self.table[self.goalIndex].x
        goalY = self.table[self.goalIndex].y
        squaredDistance = (currX - goalX)**2 + (currY - goalY)**2
        return math.sqrt(squaredDistance)

    def pop(self):
        return heappop(self.frontier)
    
    def push(self, node):
        realCost

    def initFrontier(self):
        heappush(self.frontier, (self.startIndex, 0 + self.hueristic(self.startIndex)))
        
