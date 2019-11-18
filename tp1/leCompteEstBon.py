import random


def couples(L):
    L2 = []
    for a in L:
        for b in L:
            if a != b:
                L2.append([a, b])
    return L2


def pn_moins_un(couple):
    L = []
    if couple[0] - couple[1] > 0:
        L.append([couple[0] - couple[1], str("" + str(couple[0]) + "-" + str(couple[1]))])

    L.append([couple[0] + couple[1], str("" + str(couple[0]) + "+" + str(couple[1]))])
    L.append([couple[0] * couple[1], str("" + str(couple[0]) + "*" + str(couple[1]))])
    if couple[0] % couple[1] == 0:
        L.append([int(couple[0] / couple[1]), str("" + str(couple[0]) + "/" + str(couple[1]))])
    return L


def atteignable(L, r):
    L2 = pn_moins_un(L)
    for i in range(len(L2)):
        if r == L2[i][0]:
            print(L2[i][1])
            return True

    return False


def plaques():
    L = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
    L2 = []

    for j in range(6):
        i = random.randint(0, len(L) - 1)
        L2.append(L[i])
        L.remove(L[i])

    return L2


def R():
    return random.randint(100, 999)


def possible(Plaques, r):
    for a in couples(Plaques):
        if atteignable(a, r):
            return True

    return False


def newListe(c, p, Plaques):
    L = pn_moins_un(c)
    if p == '-':
        return Plaques.append(L[0])


def LCEB(Plaques, r):
    if possible(Plaques, r):
        return True
    for a in couples(Plaques):
        LCEB(newListe(a, '-', Plaques), r)
        LCEB(newListe(a, '+', Plaques), r)
        LCEB(newListe(a, '*', Plaques), r)
        LCEB(newListe(a, '/', Plaques), r)


LCEB(plaques(), 120)
