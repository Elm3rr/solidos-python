import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función cuadrática f(x) = x^2 + 1
def f(x):
    return x**2 + 1

# Definir los límites de integración
x_min = 0  # Límite inferior
x_max = 2  # Límite superior

# Crear el espacio para las coordenadas dentro de los límites de integración
x = np.linspace(x_min, x_max, 100)

# Crear una matriz de puntos para la rotación (capa cilíndrica)
theta = np.linspace(0, 2 * np.pi, 100)
X, Theta = np.meshgrid(x, theta)

# El radio de la rotación es el valor de la función cuadrática f(x)
Y = f(X)  # Radio de las capas cilíndricas

# Coordenadas cilíndricas para la rotación completa de la función cuadrática
X_rot = Y * np.cos(Theta)  # Coordenada X tras la rotación
Y_rot = Y * np.sin(Theta)  # Coordenada Y tras la rotación
Z_rot = X  # Usamos X para el eje Z para abarcar el rango completo de la gráfica

# Graficar la función de revolución
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie de revolución de la función cuadrática
ax.plot_surface(X_rot, Y_rot, Z_rot, cmap='viridis', alpha=0.7)

# Ahora, graficar el cilindro superpuesto
f_max = np.max(f(x))  # Encontrar el valor máximo de f(x) en el intervalo
R, Theta_cyl = np.meshgrid(np.linspace(x_min, x_max, 100), theta)

# Definir las coordenadas del cilindro
X_cyl = f_max * np.cos(Theta_cyl)  # Radio constante del cilindro en el eje X
Y_cyl = f_max * np.sin(Theta_cyl)  # Radio constante del cilindro en el eje Y
Z_cyl = R  # Extensión completa en el eje Z desde el origen hasta el límite superior

# Graficar el cilindro
ax.plot_surface(X_cyl, Y_cyl, Z_cyl, cmap='plasma', alpha=0.3)

# Etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Añadir título
ax.set_title("Superficie de revolución de la función por medio del metodo de Capas Cilíndricas")

# Mostrar la gráfica
plt.show()
