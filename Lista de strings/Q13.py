#13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random
biblioteca = ['cinderela', 'aurora', 'moana', 'bela', 'princesas', 'Disney']
chances_usuario = 6
palavra_aleatoria = random.choice(biblioteca)
palavra_sorteada = ''.join(random.sample(palavra_aleatoria, len(palavra_aleatoria)))
while chances_usuario != 0:
    print("quantidade de chances: ", chances_usuario)
    print(palavra_sorteada)
    resposta_usuario = input("Que palavra é essa?  ")
    if resposta_usuario == palavra_aleatoria:
        print("Você acertou, a palavra era: ", palavra_aleatoria)
        break
    else:
        chances_usuario -= 1