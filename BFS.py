from turtle import pos

from requests import post
from UX import Logic
from UX import State

class BFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.frontier.append((self.startState.position, self.startState.cost))


    def action(self, node, offset):
        child = self.makeNewChild(node, offset)
        addedToFrontier = self.addToFrontier(child, node)
        if addedToFrontier:
            self.table[node.position + offset].inFrontier = True


    def run(self):
        if len(self.frontier) == 0:
            print("Loose!!!!")
            return -1
        node = self.frontier.pop(0)
        node = State(node[0], node[1])
        position = node.position
        self.table[position].inFrontier = False
        self.table[position].gandalfHere = True
        self.table[position].inExplored = True
        self.explored.append((node.position, node.cost))
        matchResult = self.goalTest(node)
        if matchResult == 1:
            return -2

        if (self.checkUP(position)):
            self.action(node, -1)

        if(self.checkRight(position)):
            self.action(node, self.numberOfRows)
            
        if(self.checkDown(position)):
            self.action(node, 1)
        
        if(self.checkLeft(position)):
            self.action(node, -self.numberOfRows)
        
        return position
            