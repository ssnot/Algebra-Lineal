import numpy as np

def interpolacion_lagrange(x_puntos, y_puntos, x_val):
    """Calcula el valor de Lagrange en un punto x_val."""
    n = len(x_puntos)
    resultado = 0
    for i in range(n):
        termino = y_puntos[i]
        for j in range(n):
            if i != j:
                termino *= (x_val - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        resultado += termino
    return resultado

def calcular_splines(x, y):
    n = len(x) - 1
    h = np.diff(x)
    
    # Configuración del sistema matricial A*c = B
    A = np.zeros((n + 1, n + 1))
    B = np.zeros(n + 1)
    
    # Condiciones para Spline Natural (Segunda derivada en extremos = 0)
    A[0, 0] = 1
    A[n, n] = 1
    
    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        B[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
    
    # Resolver para c
    c = np.linalg.solve(A, B)
    
    # Calcular coeficientes a, b, d
    a = y[:-1]
    b = np.zeros(n)
    d = np.zeros(n)
    
    for i in range(n):
        b[i] = (y[i+1] - y[i])/h[i] - h[i]*(2*c[i] + c[i+1])/3
        d[i] = (c[i+1] - c[i]) / (3 * h[i])
        
    return a, b, c[:-1], d