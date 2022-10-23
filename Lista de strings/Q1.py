#01. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo

string_1= input("Digite a primeira string:")
string_2= input("Digite a segunda string:")

tamanho_str_1= len(string_1)
tamanho_str_2= len(string_2)
print(string_1 + " " + str(tamanho_str_1))
print(string_2 + " " + str(tamanho_str_2))