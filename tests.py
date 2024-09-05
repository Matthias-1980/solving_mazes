import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall = False

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertFalse(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )
        
        for j in range(num_cols):
            for i in range(num_rows):
                self.assertFalse(m1._cells[j][i].visited)

if __name__ == "__main__":
    unittest.main()