import io
import unittest

from life.__main__ import main, run
from life.grid import Grid
from life.presets import PRESETS, apply_preset, parse_pattern


def live_set(grid):
    return {
        (x, y)
        for y in range(grid.height)
        for x in range(grid.width)
        if grid.is_alive(x, y)
    }


class GridTest(unittest.TestCase):
    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            Grid(0, 5)

    def test_neighbors_wrap(self):
        g = Grid(3, 3, wrap=True)
        g.set_alive(2, 2)
        self.assertEqual(g.live_neighbors(0, 0), 1)

    def test_neighbors_no_wrap(self):
        g = Grid(3, 3, wrap=False)
        g.set_alive(2, 2)
        self.assertEqual(g.live_neighbors(0, 0), 0)

    def test_block_is_still_life(self):
        g = Grid(4, 4)
        for x, y in [(1, 1), (2, 1), (1, 2), (2, 2)]:
            g.set_alive(x, y)
        before = live_set(g)
        g.step()
        self.assertEqual(live_set(g), before)

    def test_blinker_period_two(self):
        g = Grid(5, 5)
        apply_preset(g, "blinker")
        start = live_set(g)
        g.step()
        self.assertEqual(live_set(g), {(2, 1), (2, 2), (2, 3)})
        g.step()
        self.assertEqual(live_set(g), start)

    def test_glider_translates(self):
        g = Grid(10, 10)
        apply_preset(g, "glider")
        start = live_set(g)
        for _ in range(4):
            g.step()
        self.assertEqual(live_set(g), {(x + 1, y + 1) for x, y in start})


class PresetTest(unittest.TestCase):
    def test_all_presets_place(self):
        for name, rows in PRESETS.items():
            with self.subTest(name=name):
                g = Grid(40, 20)
                apply_preset(g, name)
                self.assertEqual(g.population(), len(parse_pattern(rows)))

    def test_rows_only_valid_chars(self):
        for name, rows in PRESETS.items():
            for row in rows:
                self.assertTrue(set(row) <= {"O", "."}, name)

    def test_preset_too_big(self):
        with self.assertRaises(ValueError):
            apply_preset(Grid(5, 5), "gosper-gun")


class CliTest(unittest.TestCase):
    def test_run_stops_at_limit(self):
        g = Grid(5, 5)
        apply_preset(g, "blinker")
        out = io.StringIO()
        self.assertEqual(run(g, "blinker", 0, 3, out=out), 3)
        self.assertIn("generation: 3", out.getvalue())

    def test_unknown_preset(self):
        self.assertEqual(main(["nope"]), 2)


if __name__ == "__main__":
    unittest.main()
