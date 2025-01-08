from maze.components.Mouse import Mouse


class Game:
    def __init__(self) -> None:
        self.__maze = None
        self.__mouse = None

    @property
    def maze(self) -> list:
        return self.__maze

    @maze.setter
    def maze(self, maze) -> None:
        self.__maze = maze
        self.__mouse = Mouse(self.__maze)

    def play(self, direction) -> None:
        if self.__mouse:
            self.__mouse.move(direction)

    def are_at_exit(self) -> bool:
        if self.__mouse:
            return self.__mouse.are_at_exit()
        return False

    def display_maze(self) -> None:
        for row in self.__maze:
            print(" ".join(row))
