import matplotlib.pyplot as plt
import numpy as np
"""
Si no tienen las librerias, instálenlas con estos comandos en el cmd:
pip install matplotlib
pip install numpy
"""

coordsX = [0, 1, 2, 3]
coordsY = [0, 1, 16, 81]

n = len(coordsX) - 1

Ak = []
Bk = []
Ck = []
Dk = []

gk = []
hk = []
for k in range(0, n):
    hk.append(coordsX[k+1] - coordsX[k])

print(hk)

plt.plot(coordsX, coordsY)
plt.show()