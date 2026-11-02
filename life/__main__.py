"""Command-line entry point: python -m life"""

import argparse
import sys

from .grid import Grid
from .presets import PRESETS, apply_preset
from .render import render, status_line


def build_parser():
    parser = argparse.ArgumentParser(
        prog="life",
        description="Conway's Game of Life in the terminal.",
    )
    parser.add_argument(
        "preset",
        nargs="?",
        default="glider",
        help="starting pattern (default: glider)",
    )
    parser.add_argument("-W", "--width", type=int, default=40, help="grid width")
    parser.add_argument("-H", "--height", type=int, default=20, help="grid height")
    parser.add_argument(
        "-l", "--list", action="store_true", help="list available presets"
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.list:
        for name in PRESETS:
            print(name)
        return 0

    if args.preset not in PRESETS:
        print(f"unknown preset: {args.preset}", file=sys.stderr)
        print(f"available: {', '.join(PRESETS)}", file=sys.stderr)
        return 2

    grid = Grid(args.width, args.height)
    try:
        apply_preset(grid, args.preset)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2

    print(render(grid))
    print(status_line(args.preset, 0, grid.population()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
