import unittest
import random
from one_hot_encoder import fit_transform

class TestOHE(unittest.TestCase):
    def test_countries(self):
        actual = fit_transform(['Russia', 'USA', 'France', 'USA', 'Italy'])
        expected = [('Russia', [0, 0, 0, 1]),
                    ('USA', [0, 0, 1, 0]),
                    ('France', [0, 1, 0, 0]),
                    ('USA', [0, 0, 1, 0]),
                    ('Italy', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_numbers(self):
        actual = fit_transform([1, 2, 3, 4, 2, 3])
        expected = [(1, [0, 0, 0, 1]),
                    (2, [0, 0, 1, 0]),
                    (3, [0, 1, 0, 0]),
                    (4, [1, 0, 0, 0]),
                    (2, [0, 0, 1, 0])]
        self.assertEqual(actual, expected)

    def test_not_empty_list(self):
        res = fit_transform([random.randint(0, 5) for _ in range(random.randint(1, 10))])
        self.assertTrue(res)

    def test_no_args_error(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
