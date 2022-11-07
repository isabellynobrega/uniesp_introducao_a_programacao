#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('informe a base \n'))
expoente = int(input('informe o expoente \n'))
acumulador = 1
for c in range (0,expoente):
  acumulador = base*acumulador
print('resultado =',acumulador)