from scipy import signal
import matplotlib.pyplot as plt
import numpy

num = [10.]
den = [1., 1, 3]

G = signal.lti(num, den)
Gd = G.to_discrete(dt=0.1)

a = numpy.flip(Gd.num)
b = numpy.flip(Gd.den[1:])

tempo = 20
dt = 0.1

qtd_amostras = int(tempo/dt)

maior_tamanho = numpy.max([len(a), len(b)])

x = numpy.ones(qtd_amostras+maior_tamanho)
y = numpy.zeros(qtd_amostras+maior_tamanho)

for i in range(maior_tamanho,qtd_amostras+maior_tamanho):
	y[i] = numpy.sum(-1*b*y[i-len(b):i])+numpy.sum(x[i-len(a):i]*a)

plt.step(dt*numpy.arange(0,qtd_amostras),y[maior_tamanho:])
plt.xlabel('Tempo (Segundos)')
plt.ylabel('Amplitude')
plt.legend('Reposta ao degrau do sistema discreto')
plt.show()
