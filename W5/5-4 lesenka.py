def Stairs(n):
    if n > 1:
        Stairs(n - 1)
        print()
    for i in range(1, n + 1):
        print(i, end='')


n = int(input())
Stairs(n)
