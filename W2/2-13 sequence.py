def sequence():
    seq = int(input())
    maximum = 0
    while(seq != 0):
        if maximum < seq:
            maximum = seq
        seq = int(input())
    return maximum
print(sequence())
