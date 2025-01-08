import random
from collections import deque


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [["#" for i in range(width)] for i in range(height)]
        self.startMaze()

    def startMaze(self):
        start_x = random.randint(1, self.width - 2)
        start_y = random.randint(1, self.height - 2)
        self.maze[start_y][start_x] = " "
        self.generateMaze(start_x, start_y)

        self.maze[start_y][start_x] = "@"
        exit_x, exit_y = self.findExit()
        self.maze[exit_y][exit_x] = "E"

    def generateMaze(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                1 <= nx < self.width - 1
                and 1 <= ny < self.height - 1
                and self.maze[ny][nx] == "#"
            ):
                if self.countAdjacent(nx, ny) == 1:
                    self.maze[ny][nx] = " "
                    self.generateMaze(nx, ny)

    def countAdjacent(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        counter = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and self.maze[ny][nx] == " "
            ):
                counter += 1
        return counter

    def findExit(self):
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if self.maze[y][x] == " ":
                    return x, y

    def showMaze(self):
        for row in self.maze:
            print("".join(row))

    def convertToGraph(self):
        graph = {}
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] != "#":
                    graph[(x, y)] = []
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < self.width
                            and 0 <= ny < self.height
                            and self.maze[ny][nx] != "#"
                        ):
                            graph[(x, y)].append((nx, ny))
        return graph

    def isItPassable(self, start, exit):
        graph = self.convertToGraph()
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == exit:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node])
        return False


# Example usage
if __name__ == "__main__":
    width = 12
    height = 12
    maze = Maze(width, height)
    maze.showMaze()

    start = (1, 1)  # Character's coordinates
    exit = maze.findExit()
    print("Is the maze passable:", maze.isItPassable(start, exit))
