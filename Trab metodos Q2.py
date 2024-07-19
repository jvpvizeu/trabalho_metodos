import numpy as np
import matplotlib.pyplot as plt


#Q2a--------------------------------------------------------------------------
# Intervalo para x
x = np.linspace(0, 8, 400)

# Função original
f = 4 * np.sqrt(x)

# Polinômios de Taylor
P1 = 8 + (x - 4)
P2 = 8 + (x - 4) - (1/16) * (x - 4)**2
P3 = 8 + (x - 4) - (1/16) * (x - 4)**2 - (1/128) * (x - 4)**3
P4 = 8 + (x - 4) - (1/16) * (x - 4)**2 - (1/128) * (x - 4)**3 + (15/1024) * (x - 4)**4

# Plotando os gráficos
plt.figure(figsize=(10, 8))
plt.plot(x, f, label='$f(x) = 4\sqrt{x}$', color='black')
plt.plot(x, P1, label='$P_1(x)$', linestyle='--')
plt.plot(x, P2, label='$P_2(x)$', linestyle='--')
plt.plot(x, P3, label='$P_3(x)$', linestyle='--')
plt.plot(x, P4, label='$P_4(x)$', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinômios de Taylor da função $f(x) = 4\sqrt{x}$ em torno de $x = 4$')
plt.legend()
plt.grid(True)
plt.show()

#Q2b-----------------------------------------------------------------------------
# Função e intervalo
x = np.linspace(4, 5, 100)
f = 4 * np.sqrt(x)

# Polinômio de Taylor de grau 4
P4 = 8 + (x - 4) - (1/16) * (x - 4)**2 - (1/128) * (x - 4)**3 + (15/1024) * (x - 4)**4
f_5 = 105 / (16 * x**(9/2))

# Valor máximo da quinta derivada no intervalo
M = 105 / (16 * 4**(9/2))

# Erro exato
erro_exato = np.abs(f - P4)

# Erro estimado pela desigualdade de Taylor
erro_estimado = (M / 120) * np.abs(x - 4)**5

# Plotando os gráficos
plt.figure(figsize=(10, 6))
plt.plot(x, erro_exato, label='Erro Exato |f(x) - P4(x)|', color='blue')
plt.legend()
plt.grid(True)
plt.plot(x, erro_estimado, label='Erro Estimado $R_4(x)$', linestyle='--', color='red')
plt.xlabel('x')
plt.ylabel('Erro')
plt.title('Erro Exato e Erro Estimado da Aproximação $f(x) \approx P_4(x)$')
plt.show()