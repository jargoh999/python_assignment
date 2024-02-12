import unittest
import to_list


class to_listTest(unittest.TestCase):

    def test_sum_z(self):
        list_element = [1, 2, 3, 4, 5]
        self.assertEqual(15, to_list.SumZ(list_element))

    def test_add_all_third_element(self):
        list_element = [1, 2, 3, 4, 5]
        self.assertEqual(5, to_list.add_all_third_element(list_element))

    def test_add_all_element_in_order(self):
        list_element = [1, 2, 3, 4, 5]
        self.assertEqual(9, to_list.add_all_element_in_order(list_element))
