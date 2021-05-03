''' Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuario tentar descobrir
quall foi o número escolhido pelo computador. O programa deverá 
escrever na tela se o usuario venceu ou perdeu. '''


from time import sleep#Essa lista vai fazer o computador demorar um tempo para responder
from random import randint#Essa lista vai trazer um numero aleatoreo entre quais eu determinar ex 0 ate 5
computador = randint(0, 5)#computador pensando no numero de 0 a 5

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO....')
sleep(2)#Tempo que o computador vai demorar para pensar

if jogador == computador:#Se o numero for o mesmo do computador ele vai imprir o resultado abaixo
    print('PARABÉNS! Você conseguiu me vencer')
else:#se for outro número ele imprimirá a frase abaixo
    print('GANHEI! EU PENSEI NO NÚMERO {} E NÃO NO {}'.format(computador, jogador))


