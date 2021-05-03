print('=' * 30)
print('     LOJA SUPER BARATÃO     ')
print('=' * 30)

total = totalmil = menor = cont = 0
barato = ''
while True:
    pro = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = pro
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA '))
print(f'O total se compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')