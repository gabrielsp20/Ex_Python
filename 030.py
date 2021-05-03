''' Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR OU ÍMPAR. '''

num = int(input('Me diga um número qualquer:'))
num2 = int(input('Me diga outro numero qualquer:'))
soma = num + num2
resul = soma % 2 # Fazendo essa conta todo numero par vai da 0 e todo num 1 vai dar ímpar
if resul == 0:
    print('O número {} é PAR'.format(soma))
else:
    print('O número {} é ÍMPAR'.format(soma))
