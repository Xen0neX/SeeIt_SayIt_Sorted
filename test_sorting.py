# Arihant Kuba 14 April 2022
# This file is for unit testing the various sorting algorithms in the sorting file

import unittest
import sorting


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        result = sorting.selection_sort(input_list)
        self.assertEqual(result, [2, 3, 3, 12, 13, 16, 17, 49, 53, 66, 104])


if __name__ == '__main__':
    unittest.main()
