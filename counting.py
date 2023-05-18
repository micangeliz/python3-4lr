import math


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def x1(a, b, c):
    D = discriminant(a, b, c)
    if D > 0 or D == 0:
        return (-b + math.sqrt(D)) / (2 * a)
    elif D < 0:
        return "Нет решения"


def x2(a, b, c):
    D = discriminant(a, b, c)
    if D > 0 or D == 0:
        return (-b - math.sqrt(D)) / (2 * a)
    elif D < 0:
        return "Нет решения"
