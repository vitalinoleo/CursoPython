# criando um grafico Simples 
from matplotlib import pyplot as plt


x = [1,2,3,4,5]
y = [10,15,7,12,8]

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exemplo De Grafico')
plt.show()