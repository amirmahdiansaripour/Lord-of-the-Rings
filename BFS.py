from UX import Logic

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
        # UP
        if (self.checkUP(node, table)):
            addedToFrontier = self.addToFrontier(node, -1)
            if addedToFrontier:
                table[node - 1].inFrontier = True
        # RIGHT
        if(self.checkRight(node, table)):
            addedToFrontier = self.addToFrontier(node, self.numberOfRows)           
            if addedToFrontier:
                table[node + self.numberOfRows].inFrontier = True
        # DOWN
        if(self.checkDown(node, table)):
            addedToFrontier = self.addToFrontier(node, 1)                
            if addedToFrontier:
                table[node + 1].inFrontier = True
        # LEFT
        if(self.checkLeft(node, table)):
            addedToFrontier = self.addToFrontier(node, -self.numberOfRows)                                
            if addedToFrontier:
                table[node - self.numberOfRows].inFrontier = True
        return node
            