from scipy import signal
import matplotlib.pyplot as plt
import numpy

num = [10]
den = [1, 2, 1]

#Funcao de transferencia
lti = signal.TransferFunction(num, den)
discrete_lti = lti.to_discrete(dt=0.1)

#discrete_lti.num=[a_m, a_m-1, ..., a_0 ]
print(discrete_lti.num)

#discrete_lti.den=[b_n, b_n-1, ..., b_0 ]
print(discrete_lti.den)

dt=0.1 #Perıodo de amostragem

tempo_simulacao = 10 #Tempo maximo de simulacao

num = [3]
den = [1, 1, 3]

#Funcao de transferencia
lti = signal.TransferFunction(num, den)
discrete_lti = lti.to_discrete(dt)

a = numpy.flip(discrete_lti.num)
b = numpy.flip(discrete_lti.den[1:])

tempo = numpy.arange(0,tempo_simulacao,0.1)

maior_janela = numpy.max([len(a), len(b)])

u = numpy.ones(len(tempo) + maior_janela)
y = numpy.zeros(len(tempo) + maior_janela)

for i in range(maior_janela, len(y), 1):
    y[i]=-numpy.sum(y[i-len(b):i]*b)
    +numpy.sum(u[i-len(a):i]*a)

plt.step(tempo, y[maior_janela:])