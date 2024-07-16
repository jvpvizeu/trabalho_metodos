# Definir a funcao v(x, y)
def v(xy):
    x, y = xy
    return 2 * x * y + 2 * y

# Encontrar o minimo de v(x, y)
min_result_v = minimize(v, [0, 0], bounds=bounds)

# Encontrar o maximo de v(x, y) (minimizar o negativo da funcao)
max_result_v = minimize(lambda xy: -v(xy), [0, 0], bounds=bounds)

# Obter os valores minimos e maximos
v_min = min_result_v.fun
v_max = -max_result_v.fun

# Obter as coordenadas correspondentes aos valores minimos e maximos
min_coords_v = min_result_v.x
max_coords_v = max_result_v.x

print(f"Valor minimo de v(x, y): {v_min} em {min_coords_v}")
print(f"Valor maximo de v(x, y): {v_max} em {max_coords_v}")
