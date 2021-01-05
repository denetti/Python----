from math import ceil, floor
num = float(input())


def roundrus(num):
    if num % 1 < 0.5:
        return floor(num)
    return ceil(num)
print(roundrus(num))
