import unittest
import counting


class TestCounting(unittest.TestCase):

    def test_discriminant(self):
        self.assertEqual(counting.discriminant(3, 13, -10), 289)

    def test_x1_yes(self):
        self.assertEqual(counting.x1(2, -1, -15), 3)

    def test_x1_no(self):
        self.assertEqual(counting.x1(3, 1, 6), "Нет решения")

    def test_x2_yes(self):
        self.assertEqual(counting.x2(2, -1, -15), -2.5)

    def test_x2_no(self):
        self.assertEqual(counting.x1(3, 1, 2), "Нет решения")