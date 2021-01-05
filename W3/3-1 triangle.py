import math
a = float(input())
b = float(input())
c = float(input())


def perimeter(a, b, c):
    return (a + b + c)/2


def square(a, b, c, p):
    return(math.sqrt(p * (p - a) * (p - b) * (p - c)))
print(square(a, b, c, perimeter(a, b, c)))
