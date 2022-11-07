#23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados

final_sequencia=int(input("-digite um numero--> "))
for sequencia in range(1,final_sequencia+1):
    for dividir in range(1,sequencia+1):
        if sequencia%dividir==0:
            contarrestos=0
            contarrestos=contarrestos+1
    if contarrestos==2:
        contarrestos=0
        print(contarrestos) 