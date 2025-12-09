import unittest


class SquareTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res,40)


def area(a):
    '''Принимает длинну стороны квадрата а и возвращает площадь квадрата ''' 
    return a * a


def perimeter(a):
    '''Приниммет длинну стороны a и возвращает периметр квадрата'''
    return 4 * a
