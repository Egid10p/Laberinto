from Mouse import Mouse

matriz = [
    ["#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "#"],
    ["#", "#", " ", "#", "@", "#"], 
    ["#", " ", " ", "#", " ", "E"], 
    ["#", "#", " ", " ", " ", "#"], 
    ["#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#"]]


class Game:
    def __init__(self) -> None:
        self.__maze = None
        
    @property
    def maze(self) -> list:
        return self.__maze
    
    @maze.setter
    def maze(self, maze) -> None:
        self.__maze = maze
        
    def play(self, direction) -> None:
        mouse = Mouse(self.__maze)
        mouse.move(direction)
    
    def are_at_exit(self) -> bool:
        mouse = Mouse(self.__maze)
        return mouse.are_at_exit()
        
        
game = Game()
game.maze = matriz

while True:
    for row in game.maze:
        item_row = ""
        for i in row:
            item_row = item_row + ' ' + i
        print(item_row)
    if game.are_at_exit():
        print("El ratón ha llegado a la salida!")
        break
    else:
        game.play(input("Para donde quiere mover el raton? "))
    