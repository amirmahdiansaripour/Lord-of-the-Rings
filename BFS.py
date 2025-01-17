from turtle import pos

from requests import post
from UX import Logic
from UX import State

class BFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.frontier.append((self.startState.position, self.startState.cost))
        global pos
        pos = self.startIndex

    def pop(self):
        poppedNode = self.frontier.pop(0)
        poppedNode = State(poppedNode[0], poppedNode[1])
        return poppedNode

    def push(self, child):
        self.frontier.append((child.position, child.cost))

    def action(self, node, offset):
        child = self.makeNewChild(node, offset)
        addedToFrontier = self.checkFrontierandExplore(child, node)
        if addedToFrontier:
            self.push(child)
            self.table[node.position + offset].inFrontier = True


    def run(self):
        if len(self.frontier) == 0:
            global pos
            self.table[pos].gandalfHere = True
            return -1
        node = self.pop()
        pos = node.position

        matchResult = self.preprocessNode(node)
        if matchResult == 1:
            return -2

        if (self.checkUP(pos)):
            self.action(node, -1)

        if(self.checkRight(pos)):
            self.action(node, self.numberOfRows)
            
        if(self.checkDown(pos)):
            self.action(node, 1)
        
        if(self.checkLeft(pos)):
            self.action(node, -self.numberOfRows)
        
        return pos
            