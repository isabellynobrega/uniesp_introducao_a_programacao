#11. Altere o programa anterior para mostrar no final a soma dos números.

inicio=int(input("digite o inicio do intervalo-->"))
fim=int(input("digite o fim do intervalo-->"))
soma=0
while (inicio<fim-1):
    inicio=inicio+1
    print(inicio)
    soma=inicio+soma
    
print("a soma dos intervalos é =",soma)