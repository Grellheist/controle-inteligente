import torch

#Dados sinteticos
x = torch.randn(10)
y = 2*x**2+3

#Variavel a ser estimada
a = torch.tensor(10., requires_grad=True)
b = torch.tensor(10., requires_grad=True)

treinador = torch.optim.SGD([a, b],lr=0.01)

for i in range(1000):
	#Passagem pela estimação
	y_hat = a*x**2+b

	#Função de perda
	L = torch.mean(0.5*(y_hat-y)**2)

	#zerando o gradiente
	treinador.zero_grad()

	#Calculando o gradiente
	L.backward()

	#Gradiente descendente
	treinador.step()

print(a)
print(b)
