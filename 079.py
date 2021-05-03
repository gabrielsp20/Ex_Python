valor = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adiconar...')
    c = str(input('Quer continuar? [S/N]'))
    if c in 'Nn':
        break
print('=' * 30)
valor.sort()
print(f'Você digitou os valores {valor}')

    