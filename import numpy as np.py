#valores já inseridos dentro do array
import numpy as np
a= np.array([1,0,5,-2,-5,7])
print(a)

#inserir valores 
b= np.array([])

for i in range(0,6):
    num= int(input('informe um valor: '))
    #append serve para inserir os valores
    b= np.append(b,num)
soma= b[0]+b[1]+b[5]
print("a soma dos elementos na posição 0,1 e 5",soma)

#alterando o valor de uma posição
b[4]=100
print("alterado",b)

#mostrar os valores
for i in range(0,6):
    print("a[",i,"]",a[i])



#metodo tradicional
for i in range(5):
    if num[1]%2==0:#número par
        cont=cont + 1
        
#de forma direta
pos = np.where(b%2==0)
print(pos)
pares = b[pos]
print(pares)
