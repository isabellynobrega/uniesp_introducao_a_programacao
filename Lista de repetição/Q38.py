#38.Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
"""a)Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b)Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c)A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário."""


valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
if (
    valor < 10 or valor > 600
):  
    print("Valor inválido!")
else:
    cem = valor // 100  
    valor -= cem * 100  
    cinquenta = valor // 50  
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor  
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")