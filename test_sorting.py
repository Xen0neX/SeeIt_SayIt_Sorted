# Arihant Kuba 14 April 2022
# This file is for unit testing the various sorting algorithms in the sorting file

import unittest
import sorting

# test list and sorted version of the test list. More can be added/modified here
input_list = [16, 2, 12, 3, 53, 104, 49, 3, 17, 66, 13]
sorted_list = [2, 3, 3, 12, 13, 16, 17, 49, 53, 66, 104]

class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        # Testing selection sort with the default input and sorted lists
        result = sorting.selection_sort(input_list)
        self.assertEqual(result, sorted_list)

    def test_bubble_sort(self):
        # Testing bubble_sort with the default input and sorted lists
        result = sorting.bubble_sort(input_list)
        self.assertEqual(result, sorted_list)

    def test_recursive_buble_sort(self):
        # Testing recursive_bubble_sort with the default input and sorted lists
        result = sorting.recursive_bubble_sort(input_list)
        self.assertEqual(result, sorted_list)

if __name__ == '__main__':
    unittest.main()
