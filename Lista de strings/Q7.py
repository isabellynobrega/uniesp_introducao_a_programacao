#07. Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#a.quantos espaços em branco existem na frase.
#b.quantas vezes aparecem as vogais a, e, i, o, u.

texto = input("Digite um texto: ")
# conta espaços em branco
print("espaços:", texto.count(" "))
# conta vogais
vogais = ["a", "e", "i", "o", "u"]
for v in vogais:
 print(v, ":", texto.lower().count(v), end=" ")