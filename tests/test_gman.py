import unittest
from src.gman import GManGame


class TestGman(unittest.TestCase):
    def setUp(self):
        self.game = GManGame()

    def test_input1(self):
        self.game.init_player(2, 1, "E")
        self.game.move_player_to(4, 3)
        self.assertEqual(155, self.game.calculate_power())

    def test_input2(self):
        self.game.init_player(0, 5, "W")
        self.game.move_player_to(6, 1)
        self.assertEqual(90, self.game.calculate_power())

    def test_input3(self):
        self.game.init_player(3, 6, "N")
        self.game.move_player_to(1, 0)
        self.assertEqual(110, self.game.calculate_power())

    def test_input4(self):
        self.game.init_player(0, 5, "W")
        self.game.move_player_to(5, 5)
        self.assertEqual(140, self.game.calculate_power())

    def test_input5(self):
        self.game.init_player(3, 6, "E")
        self.game.move_player_to(3, 0)
        self.assertEqual(135, self.game.calculate_power())

    def test_input6(self):
        self.game.init_player(6, 3, "S")
        self.game.move_player_to(6, 6)
        self.assertEqual(160, self.game.calculate_power())

    def test_input7(self):
        self.game.init_player(6, 3, "S")
        self.game.move_player_to(0, 3)
        self.assertEqual(135, self.game.calculate_power())


if __name__ == "__main__":
    unittest.main()
