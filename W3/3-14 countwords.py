s = str(input())
i = 1
space = s.find(' ')
while space != -1:
    i += 1
    space = s.find(' ', space + 1)
print(i)
