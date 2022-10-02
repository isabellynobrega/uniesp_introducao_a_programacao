""" 4. O IMC- Índice de Massa Corporal -  é um critério da Organização Mundial da Saúde para indicar a condição de peso de uma pessoa.
A fórmula é IMC = peso / (altura)². Elabore um algoritmo qie leia o peso e a altura de um adulto e mostre sua condição."""

massa= float(input("Digite seu peso em quilograma:"))
altura= float(input("Digite a sua altura em metros:"))
imc= (massa/(altura**2))

if imc<18.5:
    print(f" Seu IMC é de {imc: .2f}")
    print(" Você está abaixo do pesso ideal, busque o tratamento com um especialista")
elif 18.5< imc <24.99:
    print(f" Seu IMC é de { imc:.2f}")
    print(" Você está com o peso normal")
elif 25< imc <30.00:
    print(f" Seu IMC é de {imc: .2f}")
    print("Você está com sobrepeso, busque o tratamento com um especialista")
else:
    print(f"Seu IMC é de {imc: .2f}")
    print(" Você está com obesidade, busque o tratamento com um especialista")