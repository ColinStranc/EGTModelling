from unittest import TestCase
import EGT.Model.EGTGrid as egtg


class TestEGTGrid(TestCase):
    def test_grid_created_empty(self):
        grid_size = 5
        grid = egtg.EGTGrid(grid_size)

        culture_count = grid.get_culture_count()

        self.assertTrue(culture_count == 0, "Grid created with ({0}) cultures".format(culture_count))