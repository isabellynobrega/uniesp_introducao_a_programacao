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