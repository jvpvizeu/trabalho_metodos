import numpy as np
from scipy.optimize import minimize

# Definir a funcao u(x, y)
def u(xy):
    x, y = xy
    return x**2 - y**2 + 2*x + 5

# Definir as restricoes de intervalo para x e y
bounds = [(-5, 3), (-3, 3)]

# Encontrar o minimo de u(x, y)
min_result = minimize(u, [0, 0], bounds=bounds)

# Encontrar o maximo de u(x, y) (minimizar o negativo da funcao)
max_result = minimize(lambda xy: -u(xy), [0, 0], bounds=bounds)

# Obter os valores minimos e maximos
u_min = min_result.fun
u_max = -max_result.fun

# Obter as coordenadas correspondentes aos valores minimos e maximos
min_coords = min_result.x
max_coords = max_result.x

print(f"Valor mínimo de u(x, y): {u_min} em {min_coords}")
print(f"Valor máximo de u(x, y): {u_max} em {max_coords}")
