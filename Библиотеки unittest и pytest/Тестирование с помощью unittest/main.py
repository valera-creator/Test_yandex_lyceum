import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_one_correct(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrom(self):
        self.assertEqual(reverse('ALLA'), 'ALLA')

    def test_not_palindrom(self):
        self.assertEqual(reverse('hello'), 'olleh')

    def test_wrong_type_not_iter(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iter(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
