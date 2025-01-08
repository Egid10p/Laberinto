import pytest
from maze.components.Mouse import Mouse


class TestMouse:
    def setup_method(self):
        # Configuración inicial para las pruebas
        self.maze = [
            ["#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", "@", " ", "#"],
            ["#", " ", " ", " ", "#"],
            ["#", " ", " ", "E", "#"],
            ["#", "#", "#", "#", "#"],
        ]
        self.mouse = Mouse(self.maze)

    def test_initial_position(self):
        assert self.mouse.position == [2, 2]

    def test_move_up(self):
        self.mouse.move("W")
        assert self.mouse.position == [1, 2]
        assert self.maze[2][2] == " "
        assert self.maze[1][2] == "@"

    def test_move_down(self):
        self.mouse.move("S")  # Mover hacia abajo dos veces
        assert self.mouse.position == [3, 2]  # Debería volver a la posición
        assert self.maze[1][2] == " "
        assert self.maze[3][2] == "@"

    def test_move_left(self):
        self.mouse.move("A")
        assert self.mouse.position == [2, 1]
        assert self.maze[3][2] == " "
        assert self.maze[2][1] == "@"

    def test_move_right(self):
        self.mouse.move("D")
        assert self.mouse.position == [2, 3]
        assert self.maze[3][1] == " "
        assert self.maze[2][3] == "@"

    def test_move_into_wall(self):
        self.mouse.move("A")  # Mover hacia arriba
        self.mouse.move("A")  # Mover hacia arriba
        assert self.mouse.position == [2, 1]  # La posición no debería cambiar

    def test_are_at_exit(self):
        self.mouse.move("S")  # Mover hacia arriba
        self.mouse.move("S")  # Mover hacia arriba
        assert self.mouse.are_at_exit() is True  # Debería estar en la salida

    def test_not_at_exit(self):
        assert (
            self.mouse.are_at_exit() is False
        )  # Al inicio no debería estar en la salida
