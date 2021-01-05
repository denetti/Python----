def sequence():
    count = 1
    prelast = 0
    maximum = 1
    seq = 1
    while(seq != 0):
        seq = int(input())
        if seq == prelast:
            count += 1
            if count > maximum:
                maximum = count
        else:
            prelast = seq
            count = 1
    return maximum
print(sequence())
