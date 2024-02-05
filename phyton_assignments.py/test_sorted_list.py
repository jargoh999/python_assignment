import unittest

import sorted_list


class Test_bubbleSort(unittest.TestCase):
    def test_that_function_is_not_none(self):
        self.assertIsNotNone(sorted_list)

    def test_that_function_bubble_sort_sorts(self):
        sample_input = [2, 4, 6, 1, 3, 9, 0, 5]
        sample_output = [0, 1, 2, 3, 4, 5, 6, 9]
        self.assertEqual(sorted_list.bubble_sort(sample_input), sample_output)


class Test_bubbleSort2(unittest.TestCase):
    def test_that_function_bubble_sort2_sorts(self):
        sample_input = [2, 4, 6, 1, 3, 9, 0, 5]
        sample_output = [9, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(sorted_list.bubble_sort2(sample_input), sample_output)


