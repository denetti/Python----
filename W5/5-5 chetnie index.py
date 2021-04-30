listd = list(map(int, input().split()))
l = []
for lis in range(0, len(listd), 2):
    l.append(listd[lis])

# comment print(l)
print(' '.join(map(str, l)))
