''' Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual sera a base de conversão:
-1 para Binário
-2 para octal
-3 para hexadecimal
'''
from time import sleep
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para octal
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
print('PROCESSANDO....')
sleep(2)

if opcao == 1:
    print('{} convetido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convetido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convetido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')