
# Основная идея
Основываясь на геометрических формулах, вычесляет значение площади и периметра треугольника, круга, квадрата и прямоугольника.

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c


# Файлы
## circle.py
### area(r)
Принимает радиус круга r(int) и возвращает его площадь(int)<br>
Пример:area(5) = 78.53981633974483
### perimeter(r)
Принимает радиус круга r(int) и возвращает его периметр(int)<br>
Пример: perimeter(5) = 31.41592653589793
## rectangle.py
### area(a,b)
Принимает длинны 2 сторон(a(int), b(int)) треугольника и возвращает его площадь(int)<br>
Пример:area(3,5) = 15
### perimeter(a,b)
Принимает длинны 2 сторон(a(int), b(int)) прямоугольника и возвращает его периметр(int)<br>
Пример: perimeter(3,5) = 16
## square.py
### area(a)
Принимает длинну стороны квадрата а(int) и возвращает площадь квадрата(int)<br>
Пример: area(5) = 25
### perimeter(a)
Приниммет длинну стороны a(int) и возвращает периметр квадрата(int)<br>
Пример: perimeter(5) = 20
## triangle.py
### area(a,h)
Принимает длинну стороны и длинну высоты треугольника(a(int),h(int)) и возвращает площадь(int)<br>
Пример: area(4,5) = 10
### perimeter(a,b,c)
Принимает длинны 3 сторон треугольника(a(int),b(int),c(int)) и возвращает его периметр(int)<br>
Пример: perimeter(3,4,5) = 12
# История коммитов
| Commit | Description |
| --- | --- |
| 8ba9aeb | L-03: Circle and square added |
| d078c8d | L-03: Docs added |
| cd70d95 | add rectagle.py and triangle.py |
| 13e0870 | added comments to files |


