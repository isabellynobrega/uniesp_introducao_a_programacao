#33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

quantidade=int(input("quantidade de temperaturas--> "))
temperaturas=int(input("informe as temperaturas--> "))
menor=temperaturas
maior=temperaturas
somador=temperaturas
for i in range(1,quantidade):
    temperaturas=float(input("informe as temperaturas--> "))
    somador=somador+temperaturas
    if temperaturas>maior:
        maior=temperaturas
    elif temperaturas<menor:
        menor=temperaturas
print("o maior é", maior)
print("o menor é",menor)
print("a media das temperaturas é-->",somador/quantidade)