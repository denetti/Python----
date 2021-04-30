listd = list(map(int, input().split()))
l = []
for lis in range(0, len(listd), 1):
    if listd[lis] % 2 == 0:
        l.append(listd[lis])

# comment print(l)
print(' '.join(map(str, l)))
