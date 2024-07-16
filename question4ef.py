import numpy as np
import plotly.graph_objects as go

# Define a funcao w
def w(z):
    return z**2 + 2*z + 5

# Define o dominio de x e y
x = np.linspace(-5, 3, 100)
y = np.linspace(-3, 3, 100)

# Cria uma matriz de valores de z
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

# Cria uma matriz de valores de w
W = np.zeros((len(x), len(y)), dtype=complex)
for i in range(len(x)):
    for j in range(len(y)):
        W[i][j] = w(Z[i][j])

# Cria a superficie 3D
fig = go.Figure(data=[go.Surface(x=x, y=y, z=W.real, colorscale='jet', showscale=True)])

# Plota as curvas v = 0
fig.add_trace(go.Scatter3d(x=x, y=np.zeros_like(x), z=w(x), mode='lines', line=dict(color='blue', width=3))) # Para z = x e y = 0
fig.add_trace(go.Scatter3d(x=[-1], y=[0], z=[4], mode='markers', marker=dict(size=3, color='blue'))) # Para x = -1 e y = 0

# Plota a curva u = 0
fig.add_trace(go.Scatter3d(x=[-1, -1], y=[2, -2], z=np.zeros(2), mode='lines', line=dict(color='black', width=3))) #Para x = -1 e y = +/-2

# Define o titulo e os eixos
fig.update_layout(title='z**2 + 2*z + 5', 
                 scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='u'))

# Mostra a figura
fig.show()
