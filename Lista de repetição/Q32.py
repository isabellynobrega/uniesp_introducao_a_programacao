#32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
"""Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

fatorial=int(input("informe o fatorial--> "))
print("Fatorial de:",fatorial)
somador=1
for c in range(1,fatorial+1):
    somador=somador*c
    print(c,"*")
print("=",somador)