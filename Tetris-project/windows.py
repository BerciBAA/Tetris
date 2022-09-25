import arcade
from grid import Grid


class TetrisWindow(arcade.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)
        self.center_window()
        self.grid = Grid()

    def on_draw(self):
        arcade.start_render()
        self.grid.draw_all()


win = TetrisWindow(1024, 960, "Tetris")
arcade.run()
