from maze.components.RandomMazeGenerator import Maze
from maze.components.Game import Game


def main():
    matrix = Maze(20, 10)
    game = Game()
    game.maze = matrix.maze

    while True:
        game.display_maze()
        if game.are_at_exit():
            print("El ratón ha llegado a la salida!")
            break
        else:
            direction = input("Para donde quiere mover el ratón? ")
            game.play(direction)


if __name__ == "__main__":
    main()
