import numpy as np
A= np.array([])

for i in range(0,6):
    num= int(input('informe um valor: '))
    A= np.append(A,num)
soma= A[0]+A[1]+A[5]
print("a soma dos elementos na posição 0,1 e 5",soma)

A[4]=100

for i in range(0,6):
    print("A[",i,"]",A[i])