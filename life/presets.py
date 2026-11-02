"""Built-in starting patterns. 'O' = live cell, '.' = dead cell."""

PRESETS = {
    "blinker": [
        "OOO",
    ],
    "glider": [
        ".O.",
        "..O",
        "OOO",
    ],
}


def parse_pattern(rows):
    """Return list of (x, y) offsets for live cells in a pattern."""
    return [
        (x, y)
        for y, row in enumerate(rows)
        for x, ch in enumerate(row)
        if ch == "O"
    ]


def pattern_size(rows):
    return max(len(r) for r in rows), len(rows)


def apply_preset(grid, name):
    """Place the named preset centered on the grid."""
    if name not in PRESETS:
        raise KeyError(f"unknown preset: {name}")
    rows = PRESETS[name]
    pw, ph = pattern_size(rows)
    if pw > grid.width or ph > grid.height:
        raise ValueError(
            f"preset '{name}' ({pw}x{ph}) does not fit grid "
            f"{grid.width}x{grid.height}"
        )
    ox = (grid.width - pw) // 2
    oy = (grid.height - ph) // 2
    for x, y in parse_pattern(rows):
        grid.set_alive(ox + x, oy + y)
