import unittest


class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(10,0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(10,10)
        self.assertEqual(res,50 )
    def test_perimeter(self):
        res = perimeter(3,4,5)
        self.assertEqual(res,12)



def area(a, h): 
    '''Принимает длинну стороны и длинну высоты треугольника(a,h) и возвращает площадь'''
    return a * h / 2 

def perimeter(a, b, c): 
    '''Принимает длинны 3 сторон треугольника(a,b,c) и возвращает его периметр'''
    return a + b + c 
