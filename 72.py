digite = int(input('Digite um número entre 0 a 20: '))
num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis','dezesete', 'dezoito', 'dezenove', 'vinte')

while digite > 20:
    digite = int(input('Tente novamente. Digite um número entre 0 a 20: '))
print(f'Você digitou o número {num[digite]}')

        
        