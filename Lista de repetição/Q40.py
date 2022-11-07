#40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
"""a)Código da cidade;
b)Número de veículos de passeio (em 1999);
c)Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d)Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e)Qual a média de veículos nas cinco cidades juntas;
f)Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""


codigo = int(input("Informe o código da cidade--> "))
veiculos = int(input("Informe o número de veículos de passeio--> "))
acidente = int(input("Informe o número de acidentes de transito com vitimas--> "))
acidentemaior=acidente
acidentemenor=acidente
contaveiculos=veiculos
contador=0
for c in range(0,4):
    if veiculos>2000:
        contador=contador+1
        veiculosacidente=acidente
        veiculosacidente=acidente+veiculosacidente
    codigo = int(input("Informe o código da cidade--> "))
    veiculos = int(input("Informe o número de veículos de passeio--> "))
    acidente = int(input("Informe o número de acidentes de transito com vitimas--> "))
    contaveiculos=contaveiculos+veiculos
    if acidente > acidentemaior:
        acidentemaior=acidente
        codigomaior=codigo
    elif acidente<acidentemenor:
        acidentemenor=acidente
        codigomenor=codigo
print("")        
print("-o menor indice de acidente está cidade com codigo:",codigomenor,"com",acidentemenor,"acidentes" )
print("")
print("-o maior indice de acidente está cidade com codigo:",codigomaior,"com",acidentemaior,"acidentes")
print("")
print("-as cinco cidades possuem",contaveiculos,"veiculos, com media de",contaveiculos/5,"veiculos por cidade")
print("média de acidentes de trânsito em cidades com mais de 2000 veiculos",veiculosacidente/contador)