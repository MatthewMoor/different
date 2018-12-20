import math as mt
import pandas as pd

y, m = 2.3, -0.9
alpha, beta = 2.7, 1.5
M, N = -1.6, -1.1

n, a = 10, 1.0

# ------------------------------------------------

def get_x(h):
    x = [i for i in range(n + 1)]
    for i in range(n+1):
        x[i] = i * h
    return x


def get_t(k):
    t = [i for i in range(n + 2)]
    for j in range(n+2):
        t[j] = j * k
    return t

def get_f(x):
    q = y * mt.e ** (m * x) + mt.cos(y * x)
    return q


def get_fi(t):
    q = alpha * t + mt.sin(beta * t)
    return q


def get_fi2(t):
    q = mt.e ** (N * t) + M * mt.sin(m * t) + N
    return q

# -------------------------------------------------

def get_grid(x, t, S):
    u = [[j for j in range(n + 2)] for i in range(n + 1)]

    for j in range(n+2):
        u[0][j] = get_fi(t[j])
        u[n][j] = get_fi2(t[j])

    for i in range(n+1):
        u[i][0] = get_f(x[i])

    for j in range(n+1):
        for i in range(1, n):
            u[i][j + 1] = 1.0 / 6.0 * (u[i + 1][j] + 4 * u[i][j] + u[i - 1][j])

    table_x = [i / 10 for i in range(10 + 1)]
    df = pd.DataFrame({

        'ti/xi': pd.Series(t),
        'x = ' + str(table_x[0]): pd.Series(u[0]), 'x = ' + str(table_x[1]): pd.Series(u[1]),
        'x = ' + str(table_x[2]): pd.Series(u[2]),
        'x = ' + str(table_x[3]): pd.Series(u[3]), 'x = ' + str(table_x[4]): pd.Series(u[4]),
        'x = ' + str(table_x[5]): pd.Series(u[5]),
        'x = ' + str(table_x[6]): pd.Series(u[6]), 'x = ' + str(table_x[7]): pd.Series(u[7]),
        'x = ' + str(table_x[8]): pd.Series(u[8]),
        'x = ' + str(table_x[9]): pd.Series(u[9]), 'x = ' + str(table_x[10]): pd.Series(u[10]),
        
    })
    print('S:' + str(S))
    print("Method grids")
    print(df)


def get_running(x, S):
    h = 1.0 / n
    k = h ** 2 / S
    t = [j for j in range(n+2)]

    for j in range(n+2):
        t[j] = j * k

    a = [[j for j in range(n+2)] for i in range(n+1)]
    b = [[j for j in range(n+2)] for i in range(n+1)]
    u = [[j for j in range(n+2)] for i in range(n+1)]


    for j in range(n+2):
        u[0][j] = get_fi(t[j])
        u[n][j] = get_fi2(t[j])

    for i in range(n+1):
        u[i][0] = get_f(x[i])

    for j in range(n+1):
        a[0][j + 1] = 1.0 / (2 + S)
        b[0][j + 1] = u[0][j + 1] + S * u[0][j]

    for j in range(n+1):
        for r in range(1, n+1):
            a[r][j + 1] = 1 / (2 + S - a[r - 1][j + 1])
            b[r][j + 1] = a[r - 1][j + 1] * b[r - 1][j + 1] + S * u[r][j]
        i = n - 1
        while i > 0:
            u[i][j + 1] = a[i][j + 1] * (b[i][j + 1] + u[i + 1][j + 1])
            i -= 1

    table_x = [i / 10 for i in range(10 + 1)]
    df = pd.DataFrame({

        'ti/xi': pd.Series(t),
        'x = ' + str(table_x[0]): pd.Series(u[0]), 'x = ' + str(table_x[1]): pd.Series(u[1]),
        'x = ' + str(table_x[2]): pd.Series(u[2]),
        'x = ' + str(table_x[3]): pd.Series(u[3]), 'x = ' + str(table_x[4]): pd.Series(u[4]),
        'x = ' + str(table_x[5]): pd.Series(u[5]),
        'x = ' + str(table_x[6]): pd.Series(u[6]), 'x = ' + str(table_x[7]): pd.Series(u[7]),
        'x = ' + str(table_x[8]): pd.Series(u[8]),
        'x = ' + str(table_x[9]): pd.Series(u[9]), 'x = ' + str(table_x[10]): pd.Series(u[10]),

    })
    print('Method running')
    print(df)

def main():
    h = 1.0 / n
    k = h ** 2 / 6.0  # 6.0?
    S = 6
    x = get_x(h)
    t = get_t(k)
    # First
    get_grid(x, t, S)
    get_running(x, S)
    # Second
    S = 4
    get_grid(x, t, S)
    get_running(x, S)
    # Third
    S = 16
    get_grid(x, t, S)
    get_running(x, S)

answer = main()
