import pandas 
import torch
import torch.nn as nn

# Importando dados
df = pandas.read_csv('AIDS_Classification_5000.csv')

# Convertendo para tensor
dados_torch = torch.tensor(df.values, dtype=torch.float32)

# Separando entrada e saida
X = dados_torch[:,:-1]
Y = dados_torch[:,-1]

# Separando em treinamento e teste
X_train = X[:4000,:]
X_test = X[4000:,:]
Y_train = Y[:4000]
Y_test = Y[4000:]

