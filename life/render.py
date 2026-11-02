"""Terminal rendering for the grid."""

ALIVE = "██"  # two full blocks so cells look square
DEAD = "  "

CLEAR_SCREEN = "\x1b[2J"
CURSOR_HOME = "\x1b[H"
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"


def render(grid, alive=ALIVE, dead=DEAD):
    """Return the grid as a multi-line string, framed by a border."""
    width = len(alive) * grid.width
    lines = ["+" + "-" * width + "+"]
    for row in grid.cells:
        lines.append("|" + "".join(alive if c else dead for c in row) + "|")
    lines.append("+" + "-" * width + "+")
    return "\n".join(lines)


def status_line(name, generation, population):
    return f"preset: {name}  generation: {generation}  population: {population}"
