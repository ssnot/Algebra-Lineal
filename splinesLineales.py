import matplotlib.pyplot as plt
from funciones.funcLineales import F

coordsX = [0, 1, 4, 9]
coordsY = [0, 1, 16, 81]

n = len(coordsX) - 1

for i in range(0,n):
    print(F(coordsX, coordsY, i))

plt.plot(coordsX, coordsY)
plt.show()