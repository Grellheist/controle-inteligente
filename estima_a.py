import numpy
import matplotlib.pyplot as plt

qtd_iteracoes = 1000
alpha = 0.1

a = 0.5

f = lambda x: 10*x**2

x = numpy.random.rand(1000)
y = f(x) #O que gostaria

f_a = lambda x: a*x**2  #O que está sendo gerado
grad_L = lambda x: (y-f_a(x))*(-1*x**2)

solucoes = numpy.zeros(qtd_iteracoes+1)
for i in range(qtd_iteracoes):
	solucoes[i] = a
	a = a - alpha*numpy.mean(grad_L(x))
solucoes[-1:]=a

pts = numpy.arange(-20,20,0.5)
plt.plot(pts,f(pts)) #curva real
plt.plot(pts,f_a(pts)) #curva estimada
plt.plot([pts, pts],[f(pts), f_a(pts)],'-r') #erro
plt.title('a estimado:'+str(a))
plt.show()

