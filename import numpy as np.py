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

import numpy as np

#11.
c= np.array([])

for i in range(0,10):
    #para inserir valores reais
    valor= float(input('informe um valor: '))
    c= np.append(c,valor)

negativos = np.where(c<0)
#procura e mostra os números negativos
print(c[negativos])
positivos = np.where(c>0)
#mostra e soma os valores acima de 0
print(sum(c[positivos]))

#15
B= np.array([])
n= int(input("informe quantos valores terão seu array: "))

for i in range(n):
    numB= int(input('informe um valor: '))
    #append serve para inserir os valores
    B= np.append(B,numb)

#mostrar números pares e impares
paresB = B[B%2==0]
print(paresB)
imparB= B[B%2!=0]
print(imparB)
