#25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

print("-calcular idade media da turma")
quantidade_notas=int(input("-digite a quantidade de pessoas---> "))
contadormedia=0
for x in range(1,quantidade_notas+1):
    notas=int(input("-informe a idade :\n"))
    contadormedia=contadormedia+notas
media=contadormedia/quantidade_notas
print("a média de idade da turma é-->",media)
if media<26:
    print("a turma é jovem")
elif media>26 and media<60:
    print("a turma é adulta")
else:
    print("a turma é idosa")