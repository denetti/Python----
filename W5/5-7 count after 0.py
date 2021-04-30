listd = list(map(int, input().split()))
cnt = 0
for lis in range(0, len(listd), 1):
    if listd[lis] > 0:
        cnt += 1

# comment print(l)
print(cnt)
