# Criando uma função recursiva que receba número inteiro positivo N e calcule o somatório dos números de 1 a N

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)


numero = int(input("Informe um número: "))
print("A soma é", soma(numero))

# Criando um programa em C, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn. Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função.

def potencia(k, n):
    if n == 0:
        return 1

    elif n == 1:
        return k

    else:
        return k * potencia(k, n - 1)


n = int(input("Informe o número: "))
n2 = int(input("Informe por quanto quer elevar: "))
print(potencia(n, n2))

#O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função recursiva mdc em C, que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto

def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)


x = int(input("Informe um valor: "))
y = int(input("Informe um valor: "))
print(mdc(x, y))

def mult(a,b):
    if b == 0:
        return a
    else:
        return a + (mult(a,b-1))

a = int(input("Informe um valor: "))
b = int(input("Informe um valor: "))
print(mult(a,b))
