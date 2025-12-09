import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100*math.pi)
    def test_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res,6*math.pi)




def area(r):
    '''Принимает радиус круга r и возвращает его площадь '''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга r и возвращает его периметр '''
    return 2 * math.pi * r
