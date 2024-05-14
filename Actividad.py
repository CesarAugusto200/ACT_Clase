import matplotlib.pyplot as plt
import math


datos = [0.31, 1.65, 0.99, 1.32, 1.32, 0, 1.55, 0.3, 1.65, 0.66,
         0.99, 0.66, 1.65, 0.33, 0.33, 1.32, 0.99, 0.66, 0.66, 0]


R = max(datos) - min(datos)
k = round(1 + 3.322 * math.log10(len(datos)))
A = R / k

intervalos = [i * A for i in range(k + 1)]


plt.hist(datos, bins=intervalos, edgecolor='black')
plt.title('Histograma de Consumo de Refrescos')
plt.xlabel('Cantidad de refrescos (litros)')
plt.ylabel('Frecuencia')
plt.show()
