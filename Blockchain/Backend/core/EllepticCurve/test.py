from FieldElement import FieldElement
from Point import Point
a = FieldElement(num = 0, prime = 223)
b = FieldElement(num = 7, prime = 223)
x = FieldElement(num = 192, prime = 223)
y = FieldElement(num = 105, prime = 223)

p1 = Point(x, y, a, b)
print(p1)