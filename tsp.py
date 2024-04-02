import numpy
import matplotlib.pyplot as plt

#Quantidade de cidades
n = 50

#Geração dos pontos x e y
x = numpy.random.uniform(0,1000, n)
y = numpy.random.uniform(0,1000, n)

#Geração do caminho
caminho = numpy.arange(0,n,1)
numpy.random.shuffle(caminho)


def plotar_caminho(caminho):

	plt.clf()

	#Plotar as cidades
	plt.plot(x,y, 'ks')

	#Percorrer o vetor de caminho
	for i in range(0,n-1):
		#Plota uma aresta da cidade caminho[i] até a cidade caminho[i+1]
		plt.plot([x[caminho[i]], x[caminho[i+1]]],[y[caminho[i]], y[caminho[i+1]]],'-r')
		plt.annotate(str(caminho[i]),[x[caminho[i]], y[caminho[i]]])
	#PLota a aresta da última cidade até a primeira
	plt.plot([x[caminho[n-1]], x[caminho[0]]],[y[caminho[n-1]],y[caminho[0]]],'-r')
	plt.annotate(str(caminho[n-1]),[x[caminho[n-1]], y[caminho[n-1]]])
	plt.title('Distância total: '+str(custo_antigo))
	plt.draw()
	plt.pause(1)

#Percorre o caminho, calculando a distancia entre as cidades, acumulativo
def calcula_custo(caminho):
	distancia = 0
	for i in range(0,n-1):
		distancia = distancia + numpy.sqrt((x[caminho[i]]-x[caminho[i+1]])**2+(y[caminho[i]]-y[caminho[i+1]])**2)
	distancia = distancia + numpy.sqrt((x[caminho[n-1]]-x[caminho[0]])**2+(y[caminho[n-1]]-y[caminho[0]])**2)
	return distancia


custo_antigo = calcula_custo(caminho)

for i in range(100000):

	#gerar um novo caminho
	caminho_novo = numpy.arange(0,n,1)
	numpy.random.shuffle(caminho_novo)
	custo_novo = calcula_custo(caminho_novo)

	if custo_novo<custo_antigo:
		caminho = caminho_novo
		custo_antigo = custo_novo
		plotar_caminho(caminho)

print('Melhor caminho encontrado:')
print(caminho)
