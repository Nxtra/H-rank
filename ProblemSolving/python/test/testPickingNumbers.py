from pickingNumbers import pickingNumbers
import unittest


class test_AppendAndDelete(unittest.TestCase):

    def test_pickingNumbers(self):
        list = [1, 1, 2, 2, 3, 3, 3]
        max_array_size = pickingNumbers(list)
        self.assertEqual(max_array_size, 5)
