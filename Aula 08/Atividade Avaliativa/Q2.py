""" 2. [FORBELLONE, 2022] Construa um algoritimo que, tendo como dados de entrada dois pontos quaiquer do plano,
P(x1, y1) e Q(x2,y2), imprima a distância entre eles. A formulá que efetua tal cálculo é: d= (x2 - x1)2 + (y2 - y1)2"""

import math 

x1 = float(input("Digite o valor de x1:"))
y1 = float(input("Digite o valor de y1:"))
x2 = float(input("Digite o valor de x2:"))
y2 = float(input("Digite o valor de y2:"))

D = math.sqrt((x1-y1)**2 + (x2 - y2)**2)

print(f"A distância destes pontos {x1}, {y1}, {x2} e {y2} é de: {D}")