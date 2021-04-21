a = int(input())
b = int(input())


def rangenum(a, b):
    if a < b:
        for num in range(a, b+1):
            print(num)
    else:
        for num in range(a, b-1, -1):
            print(num)

rangenum(a, b)
