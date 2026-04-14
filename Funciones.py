def F(x, y, i):
    return (y[i+1]-y[i])/(x[i+1]-x[i])

def CalculoCoeficientes(x, y):
    Ak = []
    Bk = []
    Ck = []
    Dk = []
    gk = []
    n = len(x) - 1
    hk = []
    for k in range(0, n):
        hk.append(x[k+1] - x[k])