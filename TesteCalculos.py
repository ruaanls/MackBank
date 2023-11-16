'''
#TAXA 12.122 - CDB 110% CDI







import numpy as np
import matplotlib.pyplot as plt

pmt = 200
i = 0.1238 / 12
n = 12

pv = []
total = 5000

for month in range(1, n + 1):
    total += pmt
    total *= (1 + i)
    pv.append(total)

x = np.arange(1, n + 1)
y = np.array(pv)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='Month', ylabel='Present Value',
    title='Present Value of Investment Over Time')
ax.grid()

plt.show()

'''

mensal = 200
taxaMensal = 0.1238 / 12 # (taxa / 100) /12
tempo = 12 # > EM ANOS 1 2 / 12

valores = []
atual = 5000

for meses in range(1, tempo + 1):
    atual += mensal
    atual *= (1 + taxaMensal)
    valores.append(round(atual, 2))

print(valores)



