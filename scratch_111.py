"""
Lab 1
1. Дана сторона квадрата a. Знайти його периметр P=4·a.

"""


def perimetr(a: float) -> float:
    return a * 4


a = float(input("a = "))
print(perimetr(a))
