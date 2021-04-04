def Sumofsequence():
    x = int(input())
    if x != 0:
        return x + Sumofsequence()
    else:
        return x

print(Sumofsequence())
