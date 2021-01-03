def sequence():
    maximum = 0
    count = 1
    seq = 1
    while(seq != 0):
        seq = int(input())
        if seq > maximum:
            maximum = seq
            count = 1
        elif seq == maximum:
            count += 1
    return count
print(sequence())
