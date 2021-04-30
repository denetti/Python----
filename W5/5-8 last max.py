listd = list(map(int, input().split()))
num = listd[0]
ind = 0
for cnt in range(1, len(listd), 1):
    if listd[cnt] >= num:
        num = listd[cnt]
        ind = cnt


# comment print(l)
print(num, ind)
