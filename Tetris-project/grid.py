from pprint import pprint
import letters
import arcade


class Grid:
    def __init__(self):
        self.cube_size = 64
        self.width = 12
        self.height = 15
        self.grid = self.create_logic_grid()
        self.active_letter = letters.letter_T
        self.draw_letter()

    def draw_letter(self):
        rotation = self.active_letter[1]
        for y in range(len(rotation)):
            for x in range(len(rotation[y])):
                if rotation[y][x] == 2:
                    self.set_cell(x+4, y+1, 2)

    def draw_all(self):
        self.draw_grid_lines()
        self.draw_shape()

    def draw_shape(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == 1:
                    arcade.draw_rectangle_filled(x * 64 + 32, (960 - 32) - y * 64, self.cube_size, self.cube_size, arcade.color.WHITE)
                    arcade.draw_rectangle_outline(x * 64 + 32, (960 - 32) - y * 64, self.cube_size, self.cube_size, arcade.color.BLACK)
                if self.get_cell(x, y) == 2:
                    arcade.draw_rectangle_filled(x * 64 + 32, (960 - 32) - y * 64, self.cube_size, self.cube_size,
                                                 self.active_letter["color"])
                    arcade.draw_rectangle_outline(x * 64 + 32, (960 - 32) - y * 64, self.cube_size, self.cube_size,
                                                  arcade.color.BLACK)
    def draw_grid_lines(self):
        for x in range(self.width):
            arcade.draw_lines([[x * self.cube_size, 0], [x * self.cube_size, 960]], arcade.color.WHITE, 1)
        for y in range(self.height):
            arcade.draw_lines([[0, y * self.cube_size], [768, y * self.cube_size]], arcade.color.WHITE, 1)

    def create_logic_grid(self):
        grid = []
        for y in range(self.height):
            grid.append([])
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == self.height - 1:
                    grid[y].append(1)
                else:
                    grid[y].append(0)
        return grid

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value

if __name__ == "__main__":
    g = Grid()
    pprint(g.grid)
