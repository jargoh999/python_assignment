import unittest

import sort_strng


class test_sort(unittest.TestCase):
    def test_sort_it(self):
        a = "xyz"
        b = 'abc'
        c = "abcd"
        d = 'efgh'
        assert sort_strng.sort_it(a, b) == "abz xyc"
        assert sort_strng.sort_it(c, d) == "fgcd eabh"
