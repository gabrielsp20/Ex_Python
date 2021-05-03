from random import randint
from time import sleep

print('=' * 30)
print('VAMOS JOGR PAR OU IMPAR')
print('=' * 30)
computado = randint(1, 10)
v = pi = soma = ganhou = 0

while True:
    v = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? [P/I] ')).upper()
    print('-' * 30)
    soma = v + computado
    result = soma  % 2
    if result == 0:
        if pi == 'P':
            print(f'Você jogou {v} e o computado {computado}.Total de {soma} DEU PAR')
            print('-' * 30)
            print('VOCÊ GANHOU')
            print('Vamos jogar novamente...')
            sleep(2)
            print('-' * 30)
            ganhou += 1
    else:    
        if pi == 'I':
            print('-' * 30)
            print('VOCÊ GANHOU')
            print('Vamos jogar novamente...')
            sleep(2)
            print('-' * 30)
            ganhou += 1
    if result == 0:
        if pi == 'I':
            print(f'Você jogou {v} e o computado {computado}.Total de {soma} DEU PAR')
            print('-' * 30)
            print('VOCÊ PERDEU')
            print('-' * 30)
            break
    else:    
        if pi == 'P':
            print(f'Voce jogou {v} e o computado {computado}.Total de {soma} DEU IMPAR')
            print('-' * 30)
            print('VOCÊ PERDEU.....')
            sleep(3)
            print('-' * 30)
            break
print(f'GAMER OVER! você venceu {ganhou} vezes. ') 
        
    


