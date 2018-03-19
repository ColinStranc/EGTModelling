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

    def add_culture(self, index, cooperation_strategy, punishment_strategy):
        if self.invalid_index(index):
            raise Exception("({0},{1}) invalid index, cannot create culture.".format(index[0], index[1]))

        self._grid[index[0], index[1]] = Tile.Tile()

    def invalid_index(self, index):
        if index[0] >= self._grid_size or index[1] >= self._grid_size:
            return True

        if index[0] < 0 or index[1] < 0:
            return True

        return False

