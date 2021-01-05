num = int(input())


def nod(num):
    i = 2
    while(num % i != 0):
        i += 1
    return i
print(nod(num))
