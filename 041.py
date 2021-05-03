from datetime import date
ano = int(input('Em que ano você nasceu: '))

idade = date.today().year - ano 
print('A idade do atleta é {} anos'.format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM.')
elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')