#valores já inseridos
import numpy as np
a= np.array([1,0,5,-2,-5,7])
print(a)

# para inserir valores
b= np.array([])

for i in range(0,6):
    num= int(input('informe um valor: '))
    b= np.append(b,num)
soma= b[0]+b[1]+b[5]
print("a soma dos elementos na posição 0,1 e 5",soma)

a[4]=100
print("alterado",a)

for i in range(0,6):
    print("a[",i,"]",a[i])
