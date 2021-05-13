import numpy as np

print("Fatoração LU, matrizes quadradas")
m = int(input("Introduza o número de linhas "))

matriz = np.zeros([m, m])
U = np.zeros([m, m])
L = np.zeros([m, m])
print("Introduza os elementos da matriz singular")

for lin in range(0, m):
  for col in range(0, m):
    matriz[lin, col] = (input("Elemento A["+ str(lin+1)+","+str(col+1)+"]"))
    matriz[lin, col] = float (matriz[lin, col])
    U[lin, col] = matriz[lin, col]

#Fatoração LU
for k in range(0, m):
  for lin in range(0, m):
    if (k == lin):
      L[k, lin] = 1
    if (k<lin):
      fator = (matriz[lin, k]/matriz[k][k])
      L[lin, k] = fator
      for col in range(0, m):
        matriz[lin, col] = matriz[lin, col] - (fator*matriz[k, col])
        U[lin, col] = matriz[lin, col]
print("Resultados")
print("Matriz L")
print(L)
print("Matriz U")
print(U)
