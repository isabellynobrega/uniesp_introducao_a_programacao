#12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

print('Valida e corrige número de telefone:')
numero= int(input('Telefone'))
nvoNumero=''
if len(str(numero))<8:
    diferenca=8 - len (str(numero))
    novoNumero='3'*diferenca
    numeroFormatado=novoNumero + str(numero)
    numeroFormatado=numeroFormatado[0:4]+'-'+numeroFormatado[5:]
    print('Telefone possui %d digitos. Vou adicionar o digito três na frente' %len (str(numero)))
    print('Telefone corrigido sem formatação: %d numero ')