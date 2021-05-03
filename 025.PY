''' Crie um programa que leia o nome de uma pessoas e diga se ela tem 
" Silva " no seu nome '''

nome = str(input('Qual é seu nome completo? ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))#Vai dizer se é o mesmo nome