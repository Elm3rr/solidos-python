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

# Crear una matriz de puntos para la rotación (capa cilíndrica)
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# Calcular las coordenadas del sólido de revolución con capas cilíndricas
# Aquí, Y es el radio de las capas cilíndricas y Z es la altura
Y = X  # Radio (que será el valor de x)
Z = f(X)  # Altura de cada cilindro (función evaluada en x)
R = Y * np.cos(Theta)
Z_rot = Y * np.sin(Theta)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie de revolución de f(x) usando capas cilíndricas
ax.plot_surface(R, Z_rot, Z, cmap='plasma', alpha=0.7)

# Etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Añadir título
ax.set_title("Sólido de revolución por el método de capas cilíndricas")

# Mostrar la gráfica
plt.show()
