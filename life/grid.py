"""Grid model for Conway's Game of Life."""


class Grid:
    """Fixed-size 2D grid of live/dead cells."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height
        self.cells = [[False] * width for _ in range(height)]

    def is_alive(self, x, y):
        return self.cells[y][x]

    def set_alive(self, x, y, alive=True):
        self.cells[y][x] = alive

    def population(self):
        return sum(sum(row) for row in self.cells)
