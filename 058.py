from random import randint
computador = randint(1, 10)

print(''' Sou seu computador....
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')

tot = 0 
palpite = 0
while palpite != computador:
    palpite = int(input('Qual é o seu palpite? '))
    tot += 1
    if palpite < computador:
        print('Mais...Tente mais uma vez.')
    elif palpite > computador:
        print('Menos...Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!'.format(tot))