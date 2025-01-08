import pytest
from maze.components.RandomMazeGenerator import Maze


def test_crear_laberinto():
    width = 12
    height = 12
    maze = Maze(width, height)
    assert len(maze.maze) == height
    assert len(maze.maze[0]) == width


def test_bordes_muros():
    width = 12
    height = 12
    maze = Maze(width, height)
    for x in range(width):
        assert maze.maze[0][x] == "#"
        assert maze.maze[height - 1][x] == "#"
    for y in range(height):
        assert maze.maze[y][0] == "#"
        assert maze.maze[y][width - 1] == "#"


def test_personaje_y_salida():
    width = 12
    height = 12
    maze = Maze(width, height)
    personaje_encontrado = False
    salida_encontrada = False
    for row in maze.maze:
        if "@" in row:
            personaje_encontrado = True
        if "E" in row:
            salida_encontrada = True
    assert personaje_encontrado
    assert salida_encontrada


def test_laberinto_pasable():
    width = 12
    height = 12
    maze = Maze(width, height)
    inicio = (1, 1)  # Coordenadas del personaje
    salida = maze.findExit()
    assert maze.isItPassable(inicio, salida)


if __name__ == "__main__":
    pytest.main()
