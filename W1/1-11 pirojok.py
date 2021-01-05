rubbles = int(input())
kopeiks = int(input())
numbofpirojok = int(input())


def howmuch(rubbles, kopeiks, numbofpirojok):
    rubbles = (rubbles * numbofpirojok) + (kopeiks * numbofpirojok // 100)
    kopeiks = (kopeiks * numbofpirojok % 100)
    return(print(rubbles, kopeiks))
howmuch(rubbles, kopeiks, numbofpirojok)
