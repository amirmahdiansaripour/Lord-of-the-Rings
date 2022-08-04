from UX import Logic

class DFS(Logic):
    def __init__(self, table, width, height):
        super().__init__(table, width, height)
        self.nodeToExplore = self.startState

    def DFSRun(self, node, table):
        table[node].inFrontier = False
        table[node].inExplored = True
        table[node].gandalfHere = True
        self.explored.append(node)
        matchResult = self.goalTest(node)
        
        if matchResult == 1:
            table[self.nodeToExplore].gandalfHere = True 
            return -2
        #UP
        if (table[node].Center[1] > 0 and node - 1 >= 0 and table[node - 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -1)
            if addedToFrontier:
                # table[node - 1].inFrontier = True
                # table[node - 1].gandalfHere = True 
                self.nodeToExplore = node - 1
                return node
        #RIGHT
        if(table[node].Center[0] < self.numberOfCols - 1 and node + self.numberOfRows < self.numberOfCells and table[node + self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, self.numberOfRows)           
            if addedToFrontier:
                # table[node + self.numberOfRows].inFrontier = True
                # table[node + self.numberOfRows].gandalfHere = True
                self.nodeToExplore = node + self.numberOfRows
                return node
        
        #DOWN
        if(table[node].Center[1] < self.numberOfRows - 1 and node + 1 < self.numberOfCells and table[node + 1].state != 'e'):
            addedToFrontier = self.addToFrontier(node, 1)                
            if addedToFrontier:
                # table[node + 1].inFrontier = True
                # table[node + 1].gandalfHere = True
                self.nodeToExplore = node + 1
                return node
        
        #LEFT
        if(table[node].Center[0] > 0 and node - self.numberOfRows >= 0 and table[node - self.numberOfRows].state != 'e'):
            addedToFrontier = self.addToFrontier(node, -self.numberOfRows)                                
            if addedToFrontier:
                # table[node - self.numberOfRows].inFrontier = True
                # table[node - self.numberOfRows].gandalfHere = True
                self.nodeToExplore = node - self.numberOfRows
                return node
        
        return -1

    def allNodesExpanded(self, table):
        for cell in table:
            if cell.inExplored == False:
                return False
        return True
        

    def run(self, table):
        res = self.DFSRun(self.nodeToExplore, table)
        if res == -1:
            if self.allNodesExpanded(table):
                print("Loose !!!!")
                return -1    
            self.nodeToExplore = self.startState
            return self.nodeToExplore
        return res