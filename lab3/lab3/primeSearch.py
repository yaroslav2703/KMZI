import math


def primeSearch(n, m=2):
    """
    функция для нахождения количества простых чисел на интервале
    :param n: конец интервала
    :param m: начало интервала
    :return: количество простых чисел
    """
    if m == 2:
        primesList = [i for i in range(m, n + 1)]
        for it, vt in enumerate(primesList):
            for ib, vb in enumerate(primesList):
                if vt is not vb and vb % vt == 0:
                    del primesList[ib]
                else:
                    continue
        return primesList
    else:
        sq = round(math.sqrt(n))
        primesList2 = primeSearch(sq)
        primesList = [i for i in range(m, n + 1)]
        for it, vt in enumerate(primesList2):
            for ib, vb in enumerate(primesList):
                if vt is not vb and vb % vt == 0:
                    del primesList[ib]
                else:
                    continue
        return primesList
