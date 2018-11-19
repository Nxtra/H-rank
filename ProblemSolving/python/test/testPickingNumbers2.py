from pickingNumbers import pickingNumbers
import unittest


class test_AppendAndDelete2(unittest.TestCase):

    def test_pickingNumbers(self):
        list = [1, 1, 2, 2, 3, 3, 3]
        max_length = pickingNumbers(list)
        self.assertEqual(max_length, 5)
