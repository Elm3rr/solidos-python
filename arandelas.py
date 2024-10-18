import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la primera función a rotar: f(x) = x^2 + 1
def f(x):
    return x**2 + 1

# Definir la segunda función a rotar: g(x) = 2x + 3
def g(x):
    return 2*x + 1

# Definir los límites de integración
x_min = 0  # Límite inferior
x_max = 2   # Límite superior

# Crear el espacio para las coordenadas dentro de los límites de integración
x = np.linspace(x_min, x_max, 100)

# Crear una matriz de puntos para la rotación de f(x) y g(x)
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Calcular las coordenadas del sólido de revolución para f(x)
Y_f = f(X)
Z_f = Y_f * np.sin(Theta)
R_f = Y_f * np.cos(Theta)

# Calcular las coordenadas del sólido de revolución para g(x)
Y_g = g(X)
Z_g = Y_g * np.sin(Theta)
R_g = Y_g * np.cos(Theta)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie de revolución de f(x)
ax.plot_surface(X, R_f, Z_f, cmap='plasma', alpha=0.7, rstride=10, cstride=10)

# Graficar la superficie de revolución de g(x)
ax.plot_surface(X, R_g, Z_g, cmap='viridis', alpha=0.7, rstride=10, cstride=10)

# Etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Añadir título para mayor claridad
ax.set_title("Sólidos de revolución para f(x) = x^2 + 1 y g(x) = 2x + 3")

# Mostrar la gráfica
plt.show()
