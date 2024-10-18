import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función a rotar: f(x) = x^2 + 1
def f(x):
    return x**2 + 1

# Definir los límites de integración
x_min = 0  # Límite inferior
x_max = 2   # Límite superior

# Crear el espacio para las coordenadas dentro de los límites de integración
x = np.linspace(x_min, x_max, 100)
y = f(x)

# Crear una matriz de puntos para la rotación
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Calcular las coordenadas del sólido de revolución
Y = f(X)
Z = Y * np.sin(Theta)
R = Y * np.cos(Theta)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, R, Z, cmap='plasma')

# Etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar la gráfica
plt.show()
