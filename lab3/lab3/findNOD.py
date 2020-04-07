def findNOD(a, b, c=None):
    """
    нахождение НОД чисел
    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: НОД
    """
    while True:
        a, b = b, (a - (a // b) * b)
        if b == 0:
            if c is not None:
                return findNOD(c, a)
            else:
                return a