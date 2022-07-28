import unittest
import io
import sys

from src.gman import Gman


class TestGman(unittest.TestCase):
    def test_print_power(self):
        gman = Gman.initialize(3, 3, "S")
        gman.move(6, 0)

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        gman.print_power()
        sys.stdout = sys.__stdout__
        self.assertEqual("POWER 135\n", capturedOutput.getvalue())

    def test_input1(self):
        gman = Gman.initialize(2, 1, "E")
        gman.move(4, 3)
        self.assertEqual(155, gman.power)

    def test_input2(self):
        gman = Gman.initialize(0, 5, "W")
        gman.move(6, 1)
        self.assertEqual(90, gman.power)

    def test_input3(self):
        gman = Gman.initialize(3, 6, "N")
        gman.move(1, 0)
        self.assertEqual(110, gman.power)

    def test_input4(self):
        gman = Gman.initialize(0, 5, "W")
        gman.move(5, 5)
        self.assertEqual(140, gman.power)

    def test_input5(self):
        gman = Gman.initialize(3, 6, "E")
        gman.move(3, 0)
        self.assertEqual(135, gman.power)

    def test_input6(self):
        gman = Gman.initialize(6, 3, "S")
        gman.move(6, 6)
        self.assertEqual(160, gman.power)

    def test_input7(self):
        gman = Gman.initialize(6, 3, "S")
        gman.move(0, 3)
        self.assertEqual(135, gman.power)

    def test_input8(self):
        gman = Gman.initialize(5, 5, "S")
        gman.move(5, 5)
        self.assertEqual(200, gman.power)

    def test_input9(self):
        gman = Gman.initialize(3, 3, "S")
        gman.move(6, 0)
        self.assertEqual(135, gman.power)

    def test_input10(self):
        gman = Gman.initialize(3, 3, "S")
        gman.move(0, 5)
        self.assertEqual(140, gman.power)
