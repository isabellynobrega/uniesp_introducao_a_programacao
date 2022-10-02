""" 1. [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 
2 grau (Ax² + Bx + C), sendo que os valores A, B, C são fornecidos pelo usuário. 
(considere que a equação possui duas raizes reais)."""

import math

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = math.pow(b, 2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"X1 -> {x1:.2f}")
    print(f"X2 -> {x2:.2f}")
    print(f"Delta -> {delta}")
else:
    print("Reduza os valores de A e C!")

""" 2. [FORBELLONE, 2022] Construa um algoritimo que, tendo como dados de entrada dois pontos quaiquer do plano,
P(x1, y1) e Q(x2,y2), imprima a distância entre eles. A formulá que efetua tal cálculo é: d= (x2 - x1)2 + (y2 - y1)2"""

import math 

x1 = float(input("Digite o valor de x1:"))
y1 = float(input("Digite o valor de y1:"))
x2 = float(input("Digite o valor de x2:"))
y2 = float(input("Digite o valor de y2:"))

D = math.sqrt((x1-y1)**2 + (x2 - y2)**2)

print(f"A distância destes pontos {x1}, {y1}, {x2} e {y2} é de: {D}")

""" 3. Elabore um algoritmo que leia o valor de dois números inteiros e 
a operação aritimética desejada; calcule, então, s resposta adequada. 
Utiliza os simbolos da tabela a seguir para ler qual operação aritmética escolhida."""

n1 = int(input("Digite o número 1:"))
n2 = int(input("Digite o número 2:"))
operacao = input("Qual operação você vai utilizar ( +,-,,/ ou *):")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
else:
    print("Operação inválida!")
    resultado = 0
    print("Resultado:", resultado)

""" 4. O IMC- Índice de Massa Corporal -  é um critério da Organização Mundial da Saúde para indicar a condição de peso de uma pessoa.
A fórmula é IMC = peso / (altura)². Elabore um algoritmo qie leia o peso e a altura de um adulto e mostre sua condição."""

massa= float(input("Digite seu peso em quilograma:"))
altura= float(input("Digite a sua altura em metros:"))
imc= (massa/(altura**2))

if imc<18.5:
    print(f" Seu IMC é de {imc: .2f}")
    print(" Você está abaixo do pesso ideal, busque o tratamento com um especialista")
elif 18.5< imc <24.99:
    print(f" Seu IMC é de { imc:.2f}")
    print(" Você está com o peso normal")
elif 25< imc <30.00:
    print(f" Seu IMC é de {imc: .2f}")
    print("Você está com sobrepeso, busque o tratamento com um especialista")
else:
    print(f"Seu IMC é de {imc: .2f}")
    print(" Você está com obesidade, busque o tratamento com um especialista")

""" 5. Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deve terminar quando for lido um número negativo."""

n= int(input("Quantos números?:"))
i = 0
a = 0
b = 0
c = 0
d = 0

while i<n:
    numero = int(input(" Coloque um número:"))
    i= i + 1
    print(i)
    if numero<0:
        break
    if numero >= 0 and numero <= 25:
        a= a+1
    if numero >= 26 and numero <= 50:
        b= b+1
    if numero >= 51 and numero <= 75:
        c= c+1
    if numero >= 76 and numero <= 100:
        d= d+1

    print
    ("intervalo1:",a)
    print
    ("intervalo2:",b)
    print
    ("intervalo3:",c)
    print
    ("intervalo4:",d)

""" 6. Escreva um algoritmo que leia um valor inicial A e imprima a sequencia de valores do cálculo de A!
e o seu resultado. EX:5! = 5 x 4 x 3 x 2 x 1 = 120"""

def main():
    A= int(input("Digite o valor de A:"))
    fat = 1
    i = 2
    while i <= A:
        fat = fat*1
        i = i + 1

    print("O valor de %d! é de = " %A, fat)

main()