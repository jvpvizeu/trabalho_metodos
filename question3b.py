alpha = 0.0043
rho_20 = 2.7e-8

# Definir a funcao rho(t)
def rho(t):
    return rho_20 * np.exp(alpha * (t - 20))

# Definir a aproximacao linear (Taylor de primeiro grau)
def rho_linear(t):
    return rho_20 * (1 + alpha * (t - 20))

# Definir a aproximacao quadratica (Taylor de segundo grau)
def rho_quadratic(t):
    return rho_20 * (1 + alpha * (t - 20) + 0.5 * (alpha**2) * (t - 20)**2)

# Definir o intervalo de temperatura
t = np.linspace(-250, 1000, 1000)

# Calcular os valores de rho(t) e suas aproximacoes
rho_vals = rho(t)
rho_linear_vals = rho_linear(t)
rho_quadratic_vals = rho_quadratic(t)

# Criar o grafico
plt.figure(figsize=(10, 6))
plt.plot(t, rho_vals, label=r'$\rho(t) = \rho_{20} e^{\alpha(t - 20)}$', color='blue')
plt.plot(t, rho_linear_vals, label=r'$\rho(t)$ Linear', color='red', linestyle='--')
plt.plot(t, rho_quadratic_vals, label=r'$\rho(t)$ Quadratica', color='green', linestyle=':')
plt.xlabel('Temperatura (°C)')
plt.ylabel(r'Resistividade ($\Omega \cdot m$)')
plt.title(r'Grafico de $\rho(t)$ e suas aproximacoes')
plt.legend()
plt.grid(True)
plt.show()
