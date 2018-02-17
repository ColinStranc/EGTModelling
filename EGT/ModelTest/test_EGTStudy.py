from unittest import TestCase
import EGT.Model.EGTStudy as egts


class TestEGTStudy(TestCase):
    def test_default_values(self):
        study = egts.EGTStudy()

        self.assert_default_value("grid size", egts.DFLT_GRID_SIZE, study.grid_size)
        self.assert_default_value("game reps", egts.DFLT_GAME_REPS, study.game_reps)
        self.assert_default_value("birth rate", egts.DFLT_BIRTH_MODE, study.birth_mode)
        self.assert_default_value("birth rate", egts.DFLT_BIRTH_RATE, study.birth_rate)
        self.assert_default_value("birth rate", egts.DFLT_BIRTH_COUNT, study.birth_count)
        self.assert_default_value("death rate", egts.DFLT_DEATH_RATE, study.death_rate)
        self.assert_default_value("base pay", egts.DFLT_BASE_PAY, study.base_pay)
        self.assert_default_value("game mode", egts.DFLT_PUBLIC_GOODS_GAME, study.public_goods_game)
        self.assert_default_value("mutation_rate", egts.DFLT_MUTATION_RATE, study.mutation_rate)
        self.assert_default_value("Public Goods Game", egts.DFLT_PGG_MULT, study.pgg_mult)
        self.assert_default_value("contribution costs", egts.DFLT_CONTRIBUTION_COST, study.contribution_cost)
        self.assert_default_value("cost to those punished", egts.DFLT_PUNISHED_COST, study.punished_cost)
        self.assert_default_value("cost to the punisher", egts.DFLT_PUNISHER_COST, study.punisher_cost)
        self.assert_default_value("societal threat level", egts.DFLT_SOCIETAL_THREAT, study.societal_threat)
        self.assert_default_value("turn count", egts.DFLT_TURN_COUNT, study.turn_count)
        self.assert_default_value("game max pay", egts.DFLT_GAME_MAX_PAY, study.game_max_pay)

    # This should really be a multi test that runs through all numbers up to something.
    def test_societal_threat_can_be_divisible_by_five(self):
        study = egts.EGTStudy()
        study.societal_threat = 10
        self.assertEqual(10, study.societal_threat, "Societal Threat {" + str(10) + "} not accepted.")

    def test_societal_threat_must_be_divisible_by_five(self):
        study = egts.EGTStudy()
        non_five_multiple = 7

        with self.assertRaises(Exception):
            study.societal_threat = non_five_multiple

    def test_birth_mode_is_count_or_rate(self):
        study = egts.EGTStudy()

        study.birth_mode = egts.BIRTH_MODE_COUNT
        self.assertEqual(egts.BIRTH_MODE_COUNT, study.birth_mode, "Birth mode not set to count")

        study.birth_mode = egts.BIRTH_MODE_RATE
        self.assertEqual(egts.BIRTH_MODE_RATE, study.birth_mode, "Birth mode not set to rate")

        study.birth_mode = egts.BIRTH_MODE_COUNT
        self.assertEqual(egts.BIRTH_MODE_COUNT, study.birth_mode,
                         "Birth mode not set to default ({0})".format(str(egts.DFLT_BIRTH_MODE)))

        with self.assertRaises(Exception):
            study.birth_mode = "NOT_ANYTHING_SPECIAL"

    def assert_default_value(self, attr, expected, actual):
        self.assertEqual(expected, actual, self.default_incorrect_message(attr, expected, actual))

    @staticmethod
    def default_incorrect_message(attr, expected, actual):
        return "Default " + attr + " {"\
               + str(actual) + "} did not match expected " + attr + " {" + str(expected) + "}."
