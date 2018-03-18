import numpy as np
import EGT.Model.Tile as Tile


class EGTGrid(object):
    def __init__(self, grid_size):
        self._grid_size = grid_size
        self._grid = np.empty((grid_size, grid_size), Tile.Tile)

    def get_culture_count(self):
        count = 0

        for x in range(self._grid_size):
            for y in range(self._grid_size):
                if self._grid[x, y] is not None:
                    count += 1

        return count
