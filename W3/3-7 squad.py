from math import sqrt
a, b, c = float(input()), float(input()), float(input())


def sq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif d == 0:
        print(-b/(2*a))
sq(a, b, c)
