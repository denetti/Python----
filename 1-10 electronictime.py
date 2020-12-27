minutes = int(input())
while (minutes >= 1440):
    minutes -= 1440
print(minutes // 60, ' ', minutes % 60)
