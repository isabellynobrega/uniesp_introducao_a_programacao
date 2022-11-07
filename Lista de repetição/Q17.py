#17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero=int(input("informe um numero-->"))
contar_multiplicador = numero
while contar_multiplicador>1:
	contar_multiplicador = contar_multiplicador-1
	numero=numero*contar_multiplicador
	print(numero)