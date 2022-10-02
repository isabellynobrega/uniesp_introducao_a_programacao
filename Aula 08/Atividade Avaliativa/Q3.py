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