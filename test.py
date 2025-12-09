import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = triangle.area(10,0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = triangle.area(10,10)
        self.assertEqual(res,50 )
    def test_perimeter(self):
        res = triangle.perimeter(3,4,5)
        self.assertEqual(res,12)


import square

class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_square(self):
        res = square.area(10)
        self.assertEqual(res, 100)
    def test_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res,40)

import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = rectangle.area(10,0)
        self.assertEqual(res, 0)
    def test_square(self):
        res = rectangle.area(10,10)
        self.assertEqual(res, 100)
    def test_perimeter(self):
        res = rectangle.perimeter(10,10)
        self.assertEqual(res,40)

import math
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = circle.area(10)
        self.assertEqual(res, 100*math.pi)
    def test_perimeter(self):
        res = circle.perimeter(3)
        self.assertEqual(res,6*math.pi)
