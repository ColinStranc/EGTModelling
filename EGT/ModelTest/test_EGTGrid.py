from unittest import TestCase
import EGT.Model.EGTGrid as egtg


class TestEGTGrid(TestCase):
    def test_grid_created_empty(self):
        grid = egtg.EGTGrid(5)

        culture_count = grid.get_culture_count()

        self.assertTrue(culture_count == 0, "Grid created with ({0}) cultures".format(culture_count))

    def test_cannot_add_culture_to_out_of_index_square(self):
        grid_size = 5
        grid = egtg.EGTGrid(grid_size)

        with self.assertRaises(Exception):
            grid.add_culture((7,7), "Cooperate", "Punish")

        with self.assertRaises(Exception):
            grid.add_culture((2, 7), "Cooperate", "Punish")

        with self.assertRaises(Exception):
            grid.add_culture((7, 2), "Cooperate", "Punish")

    def test_can_add_culture_to_grid(self):
        grid_size = 5
        tile_index = (0,0)

        grid = egtg.EGTGrid(grid_size)
        grid.add_culture(tile_index, "Cooperate", "Punish")

        added_cultures = 1

        self.assertEqual(added_cultures, grid.get_culture_count(),
                         "Grid reporting {0} cultures despite exactly {1} being added"
                         .format(grid.get_culture_count(), added_cultures))