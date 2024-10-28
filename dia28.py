#Criando uma função recursiva que receba número inteiro positivo N e calcule o somatório dos números de 1 a N

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

def potencia(k,n):
    if n == 0:
        return 1

    elif n == 1:
        return k

    else:
        return k * potencia(k,n-1)

#numero = int(input("Informe um número: "))
#print("A soma é", soma(numero))

n = int(input("Informe o número: "))
n2 = int(input("Informe por quanto quer elevar: "))
print(potencia(n,n2))
