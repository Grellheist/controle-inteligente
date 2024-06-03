import pandas 
import torch
import torch.nn as nn

# Dados 
num_epochs = 200
lr = 0.005
batch_size = 10

# Importando dados
df = pandas.read_csv('AIDS_Classification_5000.csv')

# Convertendo para tensor
dados_torch = torch.tensor(df.values, dtype=torch.float32)

# Separando entrada e saida
X = dados_torch[:,:-1]
X = X/X.max().max()
Y = dados_torch[:,-1]
Y = Y.to(dtype=torch.long)

# Separando em treinamento e teste
X_train = X[:4000,:]
X_test = X[4000:,:]
Y_train = Y[:4000]
Y_test = Y[4000:]

modelo = nn.Sequential(nn.Linear(22,2))

# Quem ira treinar
treinador = torch.optim.SGD(modelo.parameters(), lr=lr)

# Função de perda
loss = nn.CrossEntropyLoss()

# Iteradora de dados
def data_iter(X, Y, batch_size):
    qtd_batches = int(len(X)/batch_size)
    for i in range(qtd_batches):
        yield X[i*batch_size:(i+1)*batch_size,:], Y[i*batch_size:(i+1)*batch_size]

# Treinamento
for epoch in range(num_epochs):
    for X, Y in data_iter(X_train, Y_train, batch_size):
        Y_hat = modelo(X)
        l = loss(Y_hat, Y.squeeze())
        treinador.zero_grad()
        l.sum().backward()
        treinador.step()

    print(f'Epoch: {epoch}, Perda Treinamento: {l}')

    Y_hat_test = modelo(X_test)
    l_test = loss(Y_hat_test, Y_test.squeeze())
    print(f'Epoch: {epoch}, Perda Teste: {l_test}')

    qtd_acertos = (torch.sum(torch.argmax(Y_hat_test, dim=1) == Y_test)/1000) * 100

    print(f'Acurácia: {qtd_acertos}%')
