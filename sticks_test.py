import unittest

from sticks import *
from human_game_logic import *
from computer_game_logic import *


class TestAiGameLogic(unittest.TestCase):

    def test_initialize_drawn_list(self):
        self.assertEqual(ComputerGameLogic().initialize_drawn_list(2), [[0], [0]])

    def test_initialize_choice_list(self):
        self.assertEqual(ComputerGameLogic().initialize_choice_list(2, 2), [[1, 2], [1, 2]])

    def test_remove_sticks(self):
        self.assertEqual(ComputerGameLogic().remove_sticks(2, 3, [[0], [0]], [[1, 2, 3], [1, 2, 3]]), 1, [[0] [1]])

    def test_normal_difficulty(self):
        self.assertEqual(ComputerGameLogic().select_difficulty('normal'), [6, 8])

if __name__ == '__main__':
    unittest.main()
