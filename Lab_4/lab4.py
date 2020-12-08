import math


def func(x):
    return ((9 - x ** 2) ** 0.5) / (x ** 2)


def F(x):
    return -(((9 - x) ** 0.5) / x) - math.asin(x / 3)


def left_rectangle_rule(a, b, n=3000):
    integral = 0
    h = (b - a) / n
    x = a

    for i in range(0, n - 1):
        integral += func(x)
        x += h
    return integral * h


def newton_leibniz(a, b):
    return F(b) - F(a)


if __name__ == '__main__':
    a = 1
    b = 2
    print("left rectangle: " + str(left_rectangle_rule(a, b)))
    print("newton leibniz: " + str(newton_leibniz(a, b)))
