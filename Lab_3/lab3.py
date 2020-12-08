from math import *


def algorithm(X, G):
    approximation = 1e-3
    p = m = q = 2
    n = 2 * q + 1
    e1 = [[[0 for _ in range(m)] for _ in range(n + 1)] for _ in range(n + 1)]
    cond = 1
    while cond != 0:
        cond = 0
        for j in range(1, p):
            for i in range(m):
                X[i] = G[i](X)

        for i in range(m):
            e1[0][1][i] = X[i]
        for j in range(2 * q):
            for i in range(m):
                e1[j + 1][1][i] = X[i] = G[i](X)
            if j == 0:
                for i in range(m):
                    cond = (cond or (abs(1 - (e1[0][1][i] / e1[1][1][i]))
                                     * 100 > approximation))
                    if cond == 0:
                        return X

        for k in range(1, n):
            for j in range(n - k):
                V = [e1[j + 1][k][i] - e1[j][k][i] for i in range(m)]
                _sum = sum([V[i] ** 2 for i in range(m)])
                for i in range(m):
                    e1[j][k + 1][i] = e1[j + 1][k - 1][i] + V[i] / _sum
        for i in range(m):
            X[i] = e1[0][n][i]
    return X


if __name__ == '__main__':
    F = [lambda X: 1 - e**(-X[0]) * cos(X[1]),
         lambda X: e**(-X[0])*sin(X[1]) + 1]

    X = [0.1, 0.1]
    X = algorithm(X, F)

    F1 = 1 - e**(-X[0]) * cos(X[1]) - X[0]
    F2 = e**(-X[0])*sin(X[1]) + 1 - X[1]

    print('x1 = ', X[0], '\nx2 = ', X[1])

    print("\nПеревірка")
    print('x1 = ', F[0](X))
    print('x2 = ', F[1](X))

    print(F1)
    print(F2)
