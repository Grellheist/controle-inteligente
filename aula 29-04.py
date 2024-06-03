import torch
import matplotlib.pyplot as plt 
import numpy
import torch.nn as nn 

# Função para gerar dados sintéticos
def gera_dados(qtd_dados, w_true):
    x = torch.randn(qtd_dados, len(w_true))
    y = torch.matmul(x, w_true)
    return x,y

# Pesos reais
w_true = torch.tensor([5.5, 2.2, -1.2, 8.8, -3.9])

# Dataset
x,y = gera_dados(1000, w_true)

# Modelo de regressão linear
net = nn.Linear(5, 1)

# Quem vai atualizar os pesos
treinador = torch.optim.SGD(net.parameters(), lr=0.1)

# Quão boa a transformação está
loss = nn.MSELoss()

qtd_epochs = 30

for epochs in range(qtd_epochs):
    # Passando pelo modelo 
    y_hat = net(x)

    # Avaliando a transformação
    l = loss(y, y_hat.squeeze())

    # Zerar o gradiente
    treinador.zero_grad()

    # Calculando o gradiente
    l.mean().backward()

    # Atualizando os pesos
    treinador.step()

    print(f'Epoca: {epochs} ---> Loss: {l}')

print(w_true)
print(net.weight)
print(net.bias)