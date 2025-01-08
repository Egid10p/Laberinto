import pytest
from maze.components.RandomMazeGenerator import Maze
from maze.components.Game import Game


@pytest.fixture
def setup_game():
    matrix = Maze(20, 10)
    game = Game()
    game.maze = matrix.maze
    return game


def test_initial_maze(setup_game):
    game = setup_game
    assert game.maze is not None
    assert len(game.maze) == 10
    assert len(game.maze[0]) == 20


def test_maze_display(capsys, setup_game):
    game = setup_game
    game.display_maze()
    captured = capsys.readouterr()
    assert "@" in captured.out  # Ensure the mouse position is displayed
    assert "E" in captured.out  # Ensure the exit position is displayed


def test_are_at_exit(setup_game):
    game = setup_game
    # Ensure the mouse is not at the exit at the start
    assert not game.are_at_exit()


if __name__ == "__main__":
    pytest.main()
