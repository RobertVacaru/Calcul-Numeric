import sys

import numpy as np
import pandas.api.types
import scipy.linalg as la


def substitution_method(a, b, n):
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += a[i][j] * x[j]
        sum = b[i] - sum
        sum /= a[i][i]
        x[i] = sum
    return x


def get_diff(a, b, x, n):
    diff = []
    for i in range(0, n):
        diff.append(0)
    line = 0
    for i in a:
        sum = 0
        for j in range(0, n):
            sum += x[j] * i[j]
        diff[line] = sum
        line += 1
    for i in range(0, n):
        diff[i] -= b[i]
    return diff


def get_inv(A):
    n = len(A)
    a = np.zeros((n, 2 * n))
    for i in range(n):
        for j in range(n):
            a[i][j] = A[i][j]

    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j + n] = 1

    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(2 * n):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    for i in range(n):
        divisor = a[i][i]
        for j in range(2 * n):
            a[i][j] = a[i][j] / divisor
    c = np.zeros((n, n))
    for i in range(n):
        k = 0
        for j in range(n, 2 * n):
            c[i][k] = a[i][j]
            k += 1
    return c


def gauss_algorithm(a, b, n):
    evo = []
    evo.append(a)
    for i in range(0, n):
        if a[i][i] != 0:
            a, b = lpass(a, b, n, i)
            evo.append(a)
    return a, b, evo


def lpass(a, b, n, l):
    a = a.astype(float)
    b = b.astype(float)
    for i in range(l + 1, n):
        if a[i][l] != 0:
            f = a[i][l] / a[l][l]
            for j in range(l + 1, n):
                a[i][j] = a[i][j] - f * a[l][j]
            a[i][l] = 0
            b[i] = b[i] - f * b[l]
    return a, b


def get_norm(results):
    # sum = 0
    # for element in results:
    #     sum += pow(element, 2)
    # sum = pow(sum, 1 / 2)
    # return sum
    return la.norm(results)


def lib_solve(A, b):
    return la.solve(A, b)


def lib_inv(A):
    return la.inv(A)


def plot_matrix_evolution():
    return None
