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
        if (table[node].Center[1] > 0 and node - 1 >= 0 and table[node - 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -1)
            if addedToFrontier:
                table[node - 1].inFrontier = True
        # RIGHT
        if(table[node].Center[0] < self.numberOfCols - 1 and node + self.numberOfRows < self.numberOfCells and table[node + self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, self.numberOfRows)           
            if addedToFrontier:
                table[node + self.numberOfRows].inFrontier = True
        # DOWN
        if(table[node].Center[1] < self.numberOfRows - 1 and node + 1 < self.numberOfCells and table[node + 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, 1)                
            if addedToFrontier:
                table[node + 1].inFrontier = True
        # LEFT
        if(table[node].Center[0] > 0 and node - self.numberOfRows >= 0 and table[node - self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -self.numberOfRows)                                
            if addedToFrontier:
                table[node - self.numberOfRows].inFrontier = True
        return node
            