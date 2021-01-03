num = int(input())


def sumsqrt(num):
    i = 0
    sumx = 0
    while (i < num):
        i += 1
        sumx += i ** 2
    return sumx
print(sumsqrt(num))
