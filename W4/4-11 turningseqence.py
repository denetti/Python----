def turnsequence():
    x = int(input())
    if x != 0:
        turnsequence()
    print(x)

turnsequence()
