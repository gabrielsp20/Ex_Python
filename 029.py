''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado. 
A multa vai custar R$7,00 por cada km acima do limite.'''

vel = int(input('Qual é a velocidade atual do carro?'))

if vel > 80:
    print('Você ultrapassou o limite de 80km/h')
    multa = (vel - 80) * 7
    print('E vai levar uma multa de R${:.2f}'.format(multa))

print('Tenha um otimo dia! Dirija com segurança ')