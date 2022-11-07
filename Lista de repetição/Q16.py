#16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

x, y = 1, 1
while (x<650):
    print (x)
    soma=x+y
    x,y=y,soma