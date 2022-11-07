#14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

print("calcular quantidade de numeros impares e pares")
par=0
impar=0
for i in range(10):
    numero = int(input(" degite um numero-->: "))
    if(numero%2==0):
         par=par+1
    else:
        impar=impar+1
print("temos",par,"numeros pares")
print("temos",impar,"numeros impares")