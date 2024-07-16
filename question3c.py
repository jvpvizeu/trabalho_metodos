import numpy as np
import matplotlib.pyplot as plt

# Definir os valores de alfa e rho_20
alpha = 0.0043
rho_20 = 2.7e-8

# Definir a funcao rho(t)
def rho(t):
    return rho_20 * np.exp(alpha * (t - 20))

# Definir a aproximacao linear (Taylor de primeiro grau)
def rho_linear(t):
    return rho_20 * (1 + alpha * (t - 20))

# Definir o intervalo de temperatura
t = np.linspace(-25, 75, 1000)

# Calcular os valores de rho(t) e suas aproximacoes
rho_vals = rho(t)
rho_linear_vals = rho_linear(t)

# Calcular a diferenca relativa
relative_difference = np.abs((rho_vals - rho_linear_vals) / rho_vals)

# Encontrar os indices onde a diferenca relativa e menor ou igual a 1%
within_1_percent_indices = np.where(relative_difference <= 0.01)[0]

# Obter o intervalo de t
t_min = t[within_1_percent_indices[0]]
t_max = t[within_1_percent_indices[-1]]

# Criar o grafico
plt.figure(figsize=(10, 6))
plt.plot(t, rho_vals, label=r'$\rho(t) = \rho_{20} e^{\alpha(t - 20)}$', color='blue')
plt.plot(t, rho_linear_vals, label=r'$\rho(t)$ Linear', color='red', linestyle='--')
plt.fill_between(t, rho_linear_vals, rho_vals, where=(relative_difference <= 0.01), color='green', alpha=0.3, interpolate=True, label='Dentro de 1%')
plt.xlabel('Temperatura (°C)')
plt.ylabel(r'Resistividade ($\Omega \cdot m$)')
plt.title(r'Gráfico de $\rho(t)$ e suas aproximações com intervalo de 1%')
plt.legend()
plt.grid(True)
plt.axvline(x=t_min, color='black', linestyle=':', label=f'Tmin = {t_min:.1f} °C')
plt.axvline(x=t_max, color='black', linestyle=':', label=f'Tmax = {t_max:.1f} °C')
plt.legend()
plt.show()

print(f"Intervalo de valores onde a aproximação linear fica dentro de 1%: {t_min:.1f} °C a {t_max:.1f} °C")
