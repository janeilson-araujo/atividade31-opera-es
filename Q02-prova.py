# Exercício Python 02: Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre eles.

def operacao(a, b):
    soma = a + b
    subt = a - b and b - a
    mult = a*b
    divs = a/b and b/a
    print(soma)
    print(subt)
    print(mult)
    print(divs)

num1 = int(input("digite o 1° numero:"))
num2 = int(input("digite o 2° numero:"))

operacao(num1, num2)