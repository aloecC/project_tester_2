import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 10, "default"), "default")
        self.assertEqual(arrs.get([1, 2, 3], -1), None)
        self.assertEqual(arrs.get([1, 2, 3], 5), None)
        self.assertEqual(arrs.get([], 10, "default"), "default")
        self.assertEqual(arrs.get([1, 2, 3], -5, "default"), "default")
        self.assertEqual(arrs.get([1, 2, 3], 10, "default"), "default")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 2), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], end=2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], end=-1), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, -1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], end=10), [1, 2, 3, 4])
