import numpy as np
import random 

matriz = np.diag([1,1,1])
print(matriz)

for i in range(3):
    for j in range(3):
      matriz[i][j]= random.randint(0,100)
print(matriz)

acum=0
for i in range(3):
    for j in range(3):
        acum= acum + matriz[i][j]
        prom= acum / 9
        
print(f"Suma:{acum}")
print(f"Promedio:{prom}")
print("------mayor y menor-----")
menor=100
mayor=0
for i in range(3):
    for j in range(3):
        if matriz[i][j] > mayor:
            mayor=  matriz[i][j] 
        if matriz[i][j] < menor:
            menor = matriz[i][j] 
print(f"Mayor:{mayor}")
print(f"Menor:{menor}")
print("------diagonal-----")

for i in range(3):
    for j in range(3):
        if i==j:
            print(matriz[i][j])