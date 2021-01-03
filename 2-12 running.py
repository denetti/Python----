numdayst = int(input())
numdayfn = int(input())


def runningcnt(numdayst, numdayfn):
    i = 1
    while(numdayst < numdayfn):
        numdayst = numdayst * 1.1
        i += 1
    return i
print(runningcnt(numdayst, numdayfn))
