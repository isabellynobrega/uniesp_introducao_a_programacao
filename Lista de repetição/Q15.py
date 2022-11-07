#15. A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

Fibonacci=eval(input("informe o final da sequência-->")) 
x, y = 1, 1
for c in range(Fibonacci):
    print (x)
    soma=x+y
    x,y=y,soma