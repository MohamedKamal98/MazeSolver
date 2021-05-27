# region SearchAlgorithms


class Node:
    id = None
    up = None
    down = None
    left = None
    right = None
    previousNode = None

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    maze = []  # The 2D array Map
    rows = 0  # Number of rows
    columns = 0  # Number of columns

    def __init__(self, mazeStr):
        """ mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node"""
        self.maze = [j.split(',') for j in mazeStr.split(' ')]
        # get number of columns
        for i in mazeStr:
            if i == ',':
                self.columns += 1
            if i == ' ':
                break
        # get number of rows
        for i in mazeStr:
            if i == ' ':
                self.rows += 1
        pass

    def BFS(self):
        queue = []  # queue list of nodes for BFS
        visited = []  # list of pairs of visited nodes
        # x and y are start node indices
        x = 0
        y = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.maze[i][j] == 'S':
                    x = i
                    y = j
        currentNode = self.maze[x][y]
        n = Node(currentNode)
        n.id = (x, y)
        queue.append(n)
        while currentNode != 'E':
            n = queue.pop(0)
            x = n.id[0]
            y = n.id[1]
            self.fullPath.append((x * (self.columns + 1)) + y)
            currentNode = self.maze[x][y]
            # check up
            if x + 1 <= self.rows:
                if (x + 1, y) not in visited:
                    n.up = (x + 1, y)
                    if self.maze[x + 1][y] != '#':
                        n1 = Node(self.maze[x + 1][y])
                        n1.id = (x + 1, y)
                        n1.previousNode = n
                        queue.append(n1)
                        visited.append((x + 1, y))
            # check down
            if x - 1 >= 0:
                if (x - 1, y) not in visited:
                    n.down = (x - 1, y)
                    if self.maze[x - 1][y] != '#':
                        n1 = Node(self.maze[x - 1][y])
                        n1.id = (x - 1, y)
                        queue.append(n1)
                        n1.previousNode = n
                        visited.append((x - 1, y))
            # check left
            if y - 1 >= 0:
                if (x, y - 1) not in visited:
                    n.left = (x, y - 1)
                    if self.maze[x][y - 1] != '#':
                        n1 = Node(self.maze[x][y - 1])
                        n1.id = (x, y - 1)
                        queue.append(n1)
                        n1.previousNode = n
                        visited.append((x, y - 1))
            # check right
            if y + 1 <= self.columns:
                if (x, y + 1) not in visited:
                    n.right = (x, y + 1)
                    if self.maze[x][y + 1] != '#':
                        n1 = Node(self.maze[x][y + 1])
                        n1.id = (x, y + 1)
                        queue.append(n1)
                        n1.previousNode = n
                        visited.append((x, y + 1))
            visited.append((x, y))
        self.path.append((n.id[0] * (self.columns + 1)) + n.id[1])
        while n.value != 'S':
            n = n.previousNode
            self.path.append((n.id[0] * (self.columns + 1)) + n.id[1])
        self.path.reverse()
        return self.fullPath, self.path


# endregion
# region Search_Algorithms_Main_Fn

def SearchAlgorithm_Main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    fullPath, path = searchAlgo.BFS()
    print('**BFS**\n Full Path is: ' + str(fullPath) + "\n Path: " + str(path))


# endregion
######################## MAIN ###########################33
if __name__ == '__main__':
    SearchAlgorithm_Main()
