#28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cd=int(input("-informe a quantidade de CDs adiquiridos: \n "))
somador=0
for c in range(1,quantidade_cd+1):
    preço=float(input("-informe o preço de cada CD--> "))
    somador=somador + preço
    media=somador/quantidade_cd
print("-total investido =",somador,"$")
print("-valor gasto em cada CD =",media,"$")