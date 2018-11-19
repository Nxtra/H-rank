from AppendAndDelete import find_matching_part_index
from AppendAndDelete import find_number_of_deletes
from AppendAndDelete import get_intermediate_string
from ddt import ddt, data, unpack
import unittest

@ddt
class test_AppendAndDelete(unittest.TestCase):

    @data(("blabla", "bla", 2),
          ("b", "", -1),
          ("bla", "blabla", 2),
          ("abc", "abd", 1),
          ("aa", "a", 0),
          ("hal", "hallo", 2),
          ("yolo1234", "yolo", 3),
          ("hallo", "joe", -1))
    @unpack
    def test_find_matching_part_index(self, value1, value2, value3):
        string1 = value1
        string2 = value2
        print("testing find matching part index with string1: {} and string2: {}".format(string1, string2))
        matching_index = find_matching_part_index(string1, string2)
        self.assertEqual(matching_index, value3, "tested string1: {} and string2: {}".format(string1, string2))

    @data(("blabla", "bla", 3),
          ("abc", "abd", 1),
          ("bla", "blabla", 0),
          ("hallo", "joe", 5))
    @unpack
    def test_find_number_of_deletes(self, value1, value2, value3):
        string1 = value1
        string2 = value2
        print("testing number of deletes with string1: {} and string2: {}".format(string1, string2))
        number_of_deletes = find_number_of_deletes(value1, value2)
        self.assertEqual(number_of_deletes, value3)

    @data(("blabla", "bla", "bla"),
          ("bla", "blabla", "bla"))
    @unpack
    def test_get_intermediate_string(self, value1, value2, value3):
        string1, string2 = value1, value2
        print("testing intermediate string with string1: {} and string2: {}".format(string1, string2))
        number_of_deletes = find_number_of_deletes(string1, string2)
        new1 = get_intermediate_string(string1, number_of_deletes)
        self.assertEqual(new1, value3, "Tested with {}, new: {} is not expected: {} and number of deletes {}".format(string1, new1, value3, number_of_deletes ))
