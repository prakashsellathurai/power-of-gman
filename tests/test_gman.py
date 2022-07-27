import unittest
from src.gman import Gman


class TestGman(unittest.TestCase):
    def test_input1(self):
        gman = Gman.init(2, 1, "E")
        gman.move(4, 3)
        self.assertEqual(155, gman.power)

    def test_input2(self):
        gman = Gman.init(0, 5, "W")
        gman.move(6, 1)
        self.assertEqual(90, gman.power)

    def test_input3(self):
        gman = Gman.init(3, 6, "N")
        gman.move(1, 0)
        self.assertEqual(110, gman.power)

    def test_input4(self):
        gman = Gman.init(0, 5, "W")
        gman.move(5, 5)
        self.assertEqual(140, gman.power)

    def test_input5(self):
        gman = Gman.init(3, 6, "E")
        gman.move(3, 0)
        self.assertEqual(135, gman.power)

    def test_input6(self):
        gman = Gman.init(6, 3, "S")
        gman.move(6, 6)
        self.assertEqual(160, gman.power)

    def test_input7(self):
        gman = Gman.init(6, 3, "S")
        gman.move(0, 3)
        self.assertEqual(135, gman.power)


if __name__ == "__main__":
    unittest.main()
