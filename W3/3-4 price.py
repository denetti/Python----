price = float(input())
rub = int(price)
kop = int(round((price - rub), 2) * 100)
print(rub, kop, sep=' ')
