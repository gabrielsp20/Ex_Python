''' Faça u programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou sejá passou do tempo de alistamento.
seu programa também deverá mostrar o tempo que faltou ou que passou de prazo. '''



from datetime import date
ano = int(input('Ano de nascimento: '))

idade =  date.today().year - ano

print('Quem nasceu em {} tem {} em {}'.format(ano, idade, date.today().year))

if idade >= 18:
    print('Você ja deveria ter se alistado há {}'.format(idade - 18))
    print('Seu alistamento foi em {} anos '.format( date.today().year - (idade - 18) ))
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format((18 - idade + date.today().year  )))