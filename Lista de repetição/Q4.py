#04. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populaçãoA=80000
populaçãoB=200000
ano=0
while populaçãoA < populaçãoB:
	populaçãoA+=round((populaçãoA*3.0)/100)
	populaçãoB+=round((populaçãoB*1.5)/100)
	ano=ano+1

print("levará",ano,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoB-->",populaçãoB,"habitantes")
print("populaçãoA-->", populaçãoA,"habitantes")