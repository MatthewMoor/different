import math as mt
import pandas as pd
import numpy as np

y, m = 2.3, -0.9
alpha, beta = 2.7, 1.5
M, N = -1.6, -1.1

n, a = 10, 1.0
h = 1 / n
k = h / a


def get_x(n, h):
    x = [i for i in range(n+1)]
    for i in range(n+1):
        x[i] = i * h
    return x


def get_t(n, k):
    t = [j for j in range(n+1)]
    for j in range(n+1):
        t[j] = j * k
    return t


def get_Ux0(x):
    r = y * mt.e ** (m * x) + mt.cos(y * x)
    return r


def get_Utx0(x):
    r = alpha * mt.e ** x + beta * mt.cos(y * x)
    return r


def get_U0t(t):
    r = alpha * t + mt.sin(beta * t)
    return r


def get_Ult(t):
    r = mt.e ** (N * t) + M * mt.sin(m * t) + N
    return r


def get_grid(t, n):
    x = [i for i in range(n+1)]
    U = [[j for j in range(n + 2)] for i in range(n + 1)]

    x[0] = 0
    for i in range(1, n+1):
        x[i] = i * h

    for j in range(1, n+2):
        U[0][j] = get_U0t(x[j - 1])
        U[n][j] = get_Ult(x[j - 1])

    for i in range(1, n+1):
        U[i][1] = get_Ux0(x[i])
        U[i][0] = U[i][1] - k * get_Utx0(x[i])

    for j in range(1, n+1):
        for i in range(1, n):
            U[i][j + 1] = U[i + 1][j] + U[i - 1][j] - U[i][j - 1]

    return U


def main():
    t = np.array(get_t(n, k))
    grid = get_grid(t, n)
    x = [i/10 for i in range(10+1)] # Икасы для таблицы
    iD = [i for i in range(-1, n + 1)]
    t = np.insert(t, 0, None)
    df = pd.DataFrame({

        'id': pd.Series(iD),
        'ti/xi': pd.Series(t),
        'x = ' + str(x[0]): pd.Series(grid[0]), 'x = ' + str(x[1]): pd.Series(grid[1]),
        'x = ' + str(x[2]): pd.Series(grid[2]), 'x = ' + str(x[3]): pd.Series(grid[3]),
        'x = ' + str(x[4]): pd.Series(grid[4]), 'x = ' + str(x[5]): pd.Series(grid[5]),
        'x = ' + str(x[6]): pd.Series(grid[6]), 'x = ' + str(x[7]): pd.Series(grid[7]),
        'x = ' + str(x[8]): pd.Series(grid[8]), 'x = ' + str(x[9]): pd.Series(grid[9]),
        'x = ' + str(x[10]): pd.Series(grid[10]),

    })
    df.set_index('id', inplace=True)

    print(df)


q = main()