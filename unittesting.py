"""This is an example about how to use unittest to test code"""
import unittest


def sum(num_1, num_2):
    return abs(num_1) + num_2


class BlackBoxTest(unittest.TestCase):

    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 5

        resultado = sum(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_sum_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()
