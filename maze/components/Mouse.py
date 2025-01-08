class Mouse:
    def __init__(self, maze: list) -> None:
        self.maze = maze
        self.position = None

        self.get_position()

    def get_position(self) -> list:
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "@":
                    self.position = [row, col]
                    return self.position

    def move(self, direction: str) -> None:
        direction = direction.upper()
        if direction == "W" and not self.is_there_a_wall("W"):
            self.maze[self.position[0]][self.position[1]] = " "
            self.maze[self.position[0] - 1][self.position[1]] = "@"
        elif direction == "S" and not self.is_there_a_wall("S"):
            self.maze[self.position[0]][self.position[1]] = " "
            self.maze[self.position[0] + 1][self.position[1]] = "@"
        elif direction == "A" and not self.is_there_a_wall("A"):
            self.maze[self.position[0]][self.position[1]] = " "
            self.maze[self.position[0]][self.position[1] - 1] = "@"
        elif direction == "D" and not self.is_there_a_wall("D"):
            self.maze[self.position[0]][self.position[1]] = " "
            self.maze[self.position[0]][self.position[1] + 1] = "@"
        self.get_position()

    def is_there_a_wall(self, direction: str) -> bool:
        if direction == "W":
            if self.maze[self.position[0] - 1][self.position[1]] == "#":
                return True
        elif direction == "S":
            if self.maze[self.position[0] + 1][self.position[1]] == "#":
                return True
        elif direction == "A":
            if self.maze[self.position[0]][self.position[1] - 1] == "#":
                return True
        elif direction == "D":
            if self.maze[self.position[0]][self.position[1] + 1] == "#":
                return True
        return False

    def are_at_exit(self) -> bool:
        if (
            (self.maze[self.position[0] - 1][self.position[1]] == "E")
            or (self.maze[self.position[0] + 1][self.position[1]] == "E")
            or (self.maze[self.position[0]][self.position[1] - 1] == "E")
            or (self.maze[self.position[0]][self.position[1] + 1] == "E")
        ):
            return True
        else:
            return False
