"""Grid model for Conway's Game of Life."""


class Grid:
    """Fixed-size 2D grid of live/dead cells."""

    def __init__(self, width, height, wrap=True):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height
        self.wrap = wrap
        self.cells = [[False] * width for _ in range(height)]

    def is_alive(self, x, y):
        return self.cells[y][x]

    def set_alive(self, x, y, alive=True):
        self.cells[y][x] = alive

    def live_neighbors(self, x, y):
        """Count live cells among the 8 neighbors of (x, y)."""
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.wrap:
                    nx %= self.width
                    ny %= self.height
                elif not (0 <= nx < self.width and 0 <= ny < self.height):
                    continue
                count += self.cells[ny][nx]
        return count

    def population(self):
        return sum(sum(row) for row in self.cells)
