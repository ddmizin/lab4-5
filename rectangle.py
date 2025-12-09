import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(10,0)
        self.assertEqual(res, 0)
    def test_square(self):
        res = area(10,10)
        self.assertEqual(res, 100)
    def test_perimeter(self):
        res = perimeter(10,10)
        self.assertEqual(res,40)


def area(a, b): 
    '''Принимает длинны 2 сторон треугольника и возвращает его площадь '''
    return a * b 

def perimeter(a, b): 
    '''Принимает длинны 2 сторон прямоугольника и возвращает его периметр '''
    return (a + b)*2 
