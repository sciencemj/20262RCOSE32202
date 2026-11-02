"""Command-line entry point: python -m life"""

import argparse
import sys
import time

from .grid import Grid
from .presets import PRESETS, apply_preset
from .render import (
    CLEAR_SCREEN,
    CURSOR_HOME,
    HIDE_CURSOR,
    SHOW_CURSOR,
    render,
    status_line,
)


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
    parser.add_argument(
        "-d", "--delay", type=float, default=0.1,
        help="seconds between generations (default: 0.1)",
    )
    parser.add_argument(
        "-g", "--generations", type=int, default=0,
        help="stop after N generations (default: 0 = run forever)",
    )
    parser.add_argument(
        "--no-wrap", action="store_true",
        help="treat edges as dead instead of wrapping around",
    )
    return parser


def run(grid, name, delay, generations, out=sys.stdout):
    """Animate the grid in place until generations reached or Ctrl+C."""
    out.write(HIDE_CURSOR + CLEAR_SCREEN)
    generation = 0
    try:
        while True:
            frame = render(grid) + "\n" + status_line(
                name, generation, grid.population()
            )
            out.write(CURSOR_HOME + frame + "\n")
            out.flush()
            if generations and generation >= generations:
                break
            time.sleep(delay)
            grid.step()
            generation += 1
    except KeyboardInterrupt:
        pass
    finally:
        out.write(SHOW_CURSOR)
        out.flush()
    return generation


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

    try:
        grid = Grid(args.width, args.height, wrap=not args.no_wrap)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    try:
        apply_preset(grid, args.preset)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2

    run(grid, args.preset, args.delay, args.generations)
    return 0


if __name__ == "__main__":
    sys.exit(main())
