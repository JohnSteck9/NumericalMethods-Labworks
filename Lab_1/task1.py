import numpy as np
import math
import copy


def set_max_on_top(start_position):
    max = a[start_position][start_position]
    h = start_position
    w = start_position

    for i in range(start_position, n):
        for j in range(start_position, n):
            if max < math.fabs(a[i][j]):
                h = i
                w = j

    for i in range(start_position, n):
        a[i][w], a[i][start_position] = a[i][start_position], a[i][w]

    for i in range(start_position, n):
        a[i][w + n], a[i][start_position + n] = a[i][start_position + n], a[i][
            w + n]

    for j in range(start_position, 2 * n):
        a[h][j], a[start_position][j] = a[start_position][j], a[h][j]

    permutations[start_position][0] = h
    permutations[start_position][1] = w


def return_permutations():
    for k in range(n - 1, -1, -1):
        for i in range(k, n):
            a[i][int(permutations[k][1])], a[i][k] = a[i][k], a[i][
                int(permutations[k][1])]

        for i in range(k, n):
            a[i][int(permutations[k][1]) + n], a[i][k + n] = a[i][k + n], a[i][
                int(permutations[k][1]) + n]

        for j in range(k, 2 * n):
            a[int(permutations[k][0])][j], a[k][j] = a[k][j], \
                                                     a[int(permutations[k][0])][
                                                         j]


n = int(input('Enter order of matrix: '))
a = np.zeros((n, 2 * n))

print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j + n] = 1

b = copy.deepcopy(a)
permutations = np.zeros((n, 2))

for i in range(n):
    # set_max_on_top(i)

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(2 * n):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(n):
    divisor = a[i][i]
    for j in range(2 * n):
        a[i][j] = a[i][j] / divisor
# return_permutations()

a = a.round(3)

print('\nINVERSE MATRIX IS:')
for i in range(n):
    for j in range(n, 2 * n):
        print(a[i][j], end='\t')
    print()

print('\nBegin Matrix IS:')
for i in range(n):
    for j in range(0, n):
        print(b[i][j], end='\t')
    print()

# audit
c = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k + n] * b[k][j]

for i in c:
    print(i)
