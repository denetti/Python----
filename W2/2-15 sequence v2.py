def sequence():
    i = 0
    seq = int(input())
    while(seq != 0):
        i += 1
        seq = int(input())
    return i
print(sequence())
