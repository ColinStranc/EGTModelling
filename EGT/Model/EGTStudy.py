

BIRTH_MODE_COUNT = "COUNT"
BIRTH_MODE_RATE = "RATE"

DFLT_GRID_SIZE = 5
DFLT_GAME_REPS = 4
DFLT_BIRTH_MODE = BIRTH_MODE_COUNT
DFLT_BIRTH_RATE = 1 / (DFLT_GRID_SIZE * DFLT_GRID_SIZE)
DFLT_BIRTH_COUNT = 1
DFLT_DEATH_RATE = 0.1
DFLT_BASE_PAY = 30
DFLT_PUBLIC_GOODS_GAME = "STANDARD"
DFLT_MUTATION_RATE = 0.1
DFLT_PGG_MULT = 3
DFLT_CONTRIBUTION_COST = 1
DFLT_PUNISHED_COST = 3 / 2
DFLT_PUNISHER_COST = 1 / 2
DFLT_SOCIETAL_THREAT = 5


class EGTStudy(object):
    @property
    def societal_threat(self):
        return self._societal_threat
    
    @societal_threat.setter
    def societal_threat(self, value):
        if value % 5 != 0:
            raise Exception("Proposed societal_error {" + str() + "} must be multiple of 5")
        self._societal_threat = value

    @property
    def birth_mode(self):
        return self._birth_mode

    @birth_mode.setter
    def birth_mode(self, value):
        if (value == BIRTH_MODE_COUNT) | (value == BIRTH_MODE_RATE):
            self._birth_mode = value
        else:
            raise Exception("Unrecognized birth mode: ({0}). Recognized modes: ({1}), ({2})"
                            .format(value,BIRTH_MODE_COUNT, BIRTH_MODE_RATE))

    def __init__(self):
        self.grid_size = DFLT_GRID_SIZE
        self.game_reps = DFLT_GAME_REPS
        self._birth_mode = DFLT_BIRTH_MODE
        self.birth_rate = DFLT_BIRTH_RATE
        self.birth_count = DFLT_BIRTH_COUNT
        self.death_rate = DFLT_DEATH_RATE
        self.base_pay = DFLT_BASE_PAY
        self.pgg_mult = DFLT_PGG_MULT
        self.contribution_cost = DFLT_CONTRIBUTION_COST
        self.punished_cost = DFLT_PUNISHED_COST
        self.punisher_cost = DFLT_PUNISHER_COST
        self._societal_threat = DFLT_SOCIETAL_THREAT
        self.public_goods_game = DFLT_PUBLIC_GOODS_GAME
        self.mutation_rate = DFLT_MUTATION_RATE
