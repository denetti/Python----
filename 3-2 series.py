num = int(input())


def series(num):
    cnt = 0
    i = 1
    while i <= num:
        cnt += (1 / ((i) ** 2))
        i += 1
    return cnt
print(series(num))
