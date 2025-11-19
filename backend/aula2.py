import numpy as np

np.zeros((3, 3))      # matriz 3x3 de zeros
np.ones((2, 4))       # matriz 2x4 de uns
np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # 5 valores entre 0 e 1
np.random.rand(2, 3)  # matriz 2x3 com números aleatórios

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)    # soma elemento a elemento
print(x * y)    # multiplicação elemento a elemento
print(np.sqrt(y)) # raiz quadrada
print(np.mean(y)) # média
print(np.sum(y))  # soma total
