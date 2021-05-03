from random import choice
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
joga = (int(input('Qual é sua jogada? ')))

if joga == 0:
    joga = 'PEDRA'
elif joga == 1:
    joga = 'PAPEL'
else:
    joga = 'TESOURA'


lista = ['PEDRA', 'PAPEL', 'TESOURA']

computador = choice(lista)

print('JO')
sleep(1.5)
print('KEN')
sleep(1.5)
print('PO!!!')
sleep(1.5)
print('-=-' * 10)

print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(joga))

print('-=-' * 10)

if joga == 'PAPEL' and computador == 'PEDRA':
    print('JOGADOR VENCEU')

elif computador == 'PEDRA' and joga == 'TESOURA':
    print('COMPUTADOR VENCEU')

elif joga == 'PEDRA' and computador == 'TESOURA':
    print('JOGADOR VENCEU')

elif computador == 'PAPEL' and joga == 'PEDRA':
    print('COMPUTADOR VENCEU')

elif joga == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCEU')

elif computador == 'TESOURA' and joga == 'PAPEL':
    print('COMPUTADOR VENCEU')
else:
    print('JOGADA INVALIDA')






