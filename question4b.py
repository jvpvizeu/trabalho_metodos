import numpy as np

# Definir os intervalos para x
x_vals = np.linspace(-5, 3, 400)

# Inicializar listas para armazenar os valores reais de x e y
real_x_vals = []
real_y_vals = []

# Calcular y para cada x e filtrar os valores reais e dentro do intervalo
for x in x_vals:
    y_pos = np.sqrt(x**2 + 2*x + 5)
    y_neg = -np.sqrt(x**2 + 2*x + 5)
    
    # Verificar se os valores de y sao reais e estao no intervalo [-3, 3]
    if np.isreal(y_pos) and -3 <= y_pos <= 3:
        real_x_vals.append(x)
        real_y_vals.append(y_pos)
    
    if np.isreal(y_neg) and -3 <= y_neg <= 3:
        real_x_vals.append(x)
        real_y_vals.append(y_neg)

# Combinar os resultados em numeros complexos z = x + iy
z_vals = np.array(real_x_vals) + 1j * np.array(real_y_vals)

print(z_vals)
