string = str(input())
firstpos = string.find('f')
lastpos = len(string) - 1 - (string[::-1].find('f'))
if firstpos != -1:
    if firstpos == lastpos:
        print(firstpos)
    else:
        print(firstpos, lastpos)
