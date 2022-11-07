#35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

final_sequencia=int(input("-digite um numero--> "))
for sequencia in range(1,final_sequencia+1):
    for dividir in range(1,sequencia+1):
        if sequencia%dividir==0:
            contarrestos=0
            contarrestos=contarrestos+1
    if contarrestos==2:
        contarrestos=0
        print(contarrestos)