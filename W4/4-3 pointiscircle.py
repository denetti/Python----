x, y, xc = float(input()), float(input()), float(input())
yc, r = float(input()), float(input())


def IsPointInCicrle(x, y, xc, yc, r):
    return((x - xc) ** 2 + (y - yc) ** 2 <= r ** 2)

if IsPointInCicrle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
