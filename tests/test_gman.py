import unittest
import io
import sys

from src.game import Game

TEST_INPUTS = [
    {'input': (2, 1, "E"), 'output': (4, 3), 'expected_answer': 155},
    {'input': (0, 5, "W"), 'output': (6, 1), 'expected_answer': 90},
    {'input': (3, 6, "N"), 'output': (1, 0), 'expected_answer': 110},
    {'input': (0, 5, "W"), 'output': (5, 5), 'expected_answer': 140},
    {'input': (3, 6, "E"), 'output': (3, 0), 'expected_answer': 135},
    {'input': (6, 3, "S"), 'output': (6, 6), 'expected_answer': 160},
    {'input': (6, 3, "S"), 'output': (0, 3), 'expected_answer': 135},
    {'input': (5, 5, "S"), 'output': (5, 5), 'expected_answer': 200},
    {'input': (3, 3, "S"), 'output': (6, 0), 'expected_answer': 135},
    {'input': (3, 3, "S"), 'output': (0, 5), 'expected_answer': 140},
]

PRINT_TEST_INPUT = {
    'input': (3, 3, "S"),
    'output': (6, 0),
    'expected_string': "POWER 135\n"
}

class Testgame(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_inputs = TEST_INPUTS
        self.print_test_input = PRINT_TEST_INPUT

    def test_print_power(self):
        game = Game.initialize(*self.print_test_input['input'])
        game.move(*self.print_test_input['output'])

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        game.print_power()
        sys.stdout = sys.__stdout__
        expected_string = self.print_test_input['expected_string']
        self.assertEqual(expected_string, capturedOutput.getvalue())

    def test_multiple_inputs(self):
        for test_input in self.test_inputs:
            game = Game.initialize(*test_input['input'])
            game.move(*test_input['output'])
            self.assertEqual(test_input['expected_answer'], game.power)