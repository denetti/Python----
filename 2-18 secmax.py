def sequence():
    maximum = 0
    maxsec = 0
    seq = 1
    while(seq != 0):
        seq = int(input())
        if maximum <= seq:
            maxsec = maximum
            maximum = seq
        elif maximum > seq and maxsec < seq:
            maxsec = seq
    return maxsec
print(sequence())
