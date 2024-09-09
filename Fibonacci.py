# Exercício 4: Imprimir uma sequência de Fibonacci

n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a = 1
b = 1
print("Sequência de Fibonacci com", n, "termos:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
