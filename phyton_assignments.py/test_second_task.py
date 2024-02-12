import unittest
import second_task


class Test(unittest.TestCase):
    def test_remove_item(self):
        list_to_test = [1, 2, 3, 4]
        list_actual = second_task.remove_item(1, list_to_test)
        list_expected = [2, 3, 4]
        assert list_actual == list_expected

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4, 5, 6, 8, 9}
        set2 = {1, 2, 3, 4, 9, 0, 6, 4}
        sets = second_task.find_intersection(set1, set2)
        setA = {1, 2, 3, 4, 6, 9}
        assert sets == setA
