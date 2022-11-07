#27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turma=int(input("informe a quantidade de turma:\n"))
alunos1=0
for c in range(1,turma+1):
    alunos=int(input("informe a quantidade de alunos em cada turma-->"))
    while alunos>40:
        alunos=int(input("valor incorreto,informe novamente a quantidade de alunos em cada turma-->"))
    alunos1=alunos1+alunos
media_alunos= (alunos1)/turma
print(media_alunos)