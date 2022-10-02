""" 6. Escreva um algoritmo que leia um valor inicial A e imprima a sequencia de valores do cálculo de A!
e o seu resultado. EX:5! = 5 x 4 x 3 x 2 x 1 = 120"""

def main():
    A= int(input("Digite o valor de A:"))
    fat = 1
    i = 2
    while i <= A:
        fat = fat*1
        i = i + 1

    print("O valor de %d! é de = " %A, fat)

main()