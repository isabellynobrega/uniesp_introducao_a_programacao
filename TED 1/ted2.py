""" exercicio 1: As maçãs custam R$1,30 cada se forem compradas menos de uma duzia, e R$1,00 se forem compradas pelo menos 12.
Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
"""

print("[!] Oferta: Na compra de 12 maçãs, a unidade sai de R$1,30 por R$1,00. [!] ")
maçãs= int (input("Digite a quantidade de maçãs que deseja comprar (0 para fechar do programa):"))

preço_oferta=1.00
preço_normal=1.30

if maçãs == 0: # caso o cliente queira encerrar 
    print(" já vai?")
    exit(0)
elif maçãs< 0: #caso o cliente coloque um numero negativo, mostrar (ERRO)
    print(f " Número negativo, não conseguimos realizar a compra: {maçãs}")
    exit(1)
elif maçãs>= 12: # A oferta será aplicada
    total = preço_oferta * maçãs
    print(f" Você realizou a compra de {maças} e conseguiu nossa oferta . Valor total de : R$ {total}")
else: # Valor sem aplicação da oferta
    total= preço_normal * maçãs
    print(f" Você comprou {maçãs} e infelismente não conseguimos te dar a oferta. valor total de: R$ {total}")