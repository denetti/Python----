def sequence():
    i = 0
    seq = 1
    while(seq != 0):
        seq = int(input())
        if (seq % 2 == 0) and (seq != 0):
            i += 1
    return i
print(sequence())
