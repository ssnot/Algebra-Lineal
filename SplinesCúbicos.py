import matplotlib.pyplot as plt
import numpy as np
from Funciones import F
"""
Si no tienen las librerias, instálenlas con estos comandos en el cmd:
pip install matplotlib
pip install numpy
"""

coordsX = [0, 1, 4, 9]
coordsY = [0, 1, 16, 81]

n = len(coordsX) - 1

for i in range(0,n):
    print(F(coordsX, coordsY, i))

plt.plot(coordsX, coordsY)
plt.show()