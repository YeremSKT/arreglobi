import numpy as np

matriz = np.five((3,3),dtype=int)
print(matriz)
cont=1

for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j]= cont
            cont=cont+1
            
print(matriz)