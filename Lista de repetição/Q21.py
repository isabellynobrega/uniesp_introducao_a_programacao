#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num=int(input("-Digite Um Numero--> "))        
contaresto=0        
for c in range(1,num+1):        
    resto=num%c    
    if resto==0:        
        contaresto=contaresto+1    
if contaresto==1 or contaresto==2:
    print(num,"é primo")
else:
    print(num,"nao é primo")