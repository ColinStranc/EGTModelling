import unittest
from EGT.Model import Tile


class EGTTileTest(unittest.TestCase):
    def test_set_culture(self):
        t = Tile.Tile()
        test_culture = "tc";

        t.set_culture(test_culture)

        self.assertEqual(test_culture, t.get_culture(), "Culture not returned properly")