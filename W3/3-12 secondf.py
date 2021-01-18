s = str(input())
a = s.find('f')


def secondelf(a):
    while a != -1:
        if s.find('f', a + 1) == -1:
            return(-1)
        else:
            return(s.find('f', a + 1))
            break
if a == -1:
    print(-2)
elif a != -1:
    print(secondelf(a))
