import numpy as np
import math as mt
import pandas as pd
n1, n2 = 10, 20
h1, h2 = 1.0 / 10, 1.0 / 20
alpha0, alpha1 = 1.0, 1.0
beta0, beta1 = -2.0, 4.0
A, B = 1, 1.7

def getp(x):
    return -x
         
def getq(x):
    return mt.sin(x)
    
def getf(x):
    return x
    
def getx(n, h):
    x = [i for i in range(n+1)]
    x[0] = 0
    for i in range(1, n+1):
        x[i] = x[i - 1] + h
    return x

def getm(n, h, x):
    m = [i for i in range(n)]
    for i in range(1, n):
        m[i] = (2 * h * h * getq(x[i]) - 4) / (2 + h * getp(x[i]))
    return m
    
def getr(n, h, x):
    r = [i for i in range(n)]
    for i in range(1, n):
        r[i] = (2 - h * getp(x[i])) / (2 + h * getp(x[i]))
    return r
    
def getfi(n, h, x):
    fi = [i for i in range(n)]
    for i in range(0, n):
        fi[i] = (2 * h**2 * getf(x[i])) / (2 + h * getp(x[i]))
    return fi
    
def getc(n, h, m, r):
    c = [i for i in range(n)]
    c[0] = alpha0 / (h * alpha1 - alpha0)
    for i in range(1, n):
        c[i] = 1.0 / (m[i] - r[i] * c[i - 1])
    return c
    
def getd(n, h, r, fi, c):
    d = [i for i in range(n)]
    d[0] = A * h / alpha0
    for i in range(1, n):
        d[i] = fi[i] - r[i] * c[i - 1] * d[i - 1]
    return d
    
def gety(n, h, c, d):
    y = [i for i in range(n+1)]
    y[n] = (B * h + beta0 * c[n - 1] * d[n - 1]) / (beta0 * (1 + c[n - 1]) + h * beta1)
    for i in reversed(range(0, n)):
        y[i] = c[i] * (d[i] - y[i + 1])
    return y

def main():
    x = np.array(getx(n1, h1))
    m = np.array(getm(n1, h1, x))
    r = np.array(getr(n1, h1, x))
    fi = np.array(getfi(n1, h1, x))
    c = np.array(getc(n1, h1, m, r))
    d = np.array(getd(n1, h1, r, fi, c))
    y = np.array(gety(n1, h1, c, d))
    df = pd.DataFrame({'x': pd.Series(x), 'y': pd.Series(y), 'm': pd.Series(m[0:10]),
                       'r': pd.Series(r[0:10]), 'fi': pd.Series(fi[0:10]), 'c': pd.Series(c[0:10]),
                       'd': pd.Series(d[0:10]), })
    df = df[['x', 'y', 'm', 'r', 'fi', 'c', 'd']]
    df.index.name = 'n'
    print(df)
    y0 = (A * h1 - alpha0 * y[1]) / (h1 * alpha1 - alpha0)
    print("\n y0 = " + str(y0))
    print(' y0 - y[0] = ', abs(y0 - y[0]), '\n')
    
    x2 = np.array(getx(n2, h2))
    m2 = np.array(getm(n2, h2, x2))
    r2 = np.array(getr(n2, h2, x2))
    fi2 = np.array(getfi(n2, h2, x2))
    c2 = np.array(getc(n2, h2, m2, r2))
    d2 = np.array(getd(n2, h2, r2, fi2, c2))
    y2 = np.array(gety(n2, h2, c2, d2))
    
    
    df = pd.DataFrame({'x': pd.Series(x2), 'y': pd.Series(y2), 'm': pd.Series(m2[0:20]),
                       'r': pd.Series(r2[0:20]), 'fi': pd.Series(fi2[0:20]), 'c': pd.Series(c2[0:20]),
                       'd': pd.Series(d2[0:20]), })
    df.index.name = 'n'
    print(df[['x', 'y', 'm', 'r', 'fi', 'c', 'd']])
    
    y02 = (A * h2 - alpha0 * y2[1]) / (h2 * alpha1 - alpha0)
    print("\n y0 = " + str(y02))
    print(' y0 - y[0] = ', abs(y02 - y2[0]), '\n')
q = main()
