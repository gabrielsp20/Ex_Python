print('=' * 10, 'LOJAS GABRIEL' ,'=' * 10)

val = (float(input('Preço das compras: R$')))

print(''' FORMAS DE PAGAMENTOS 
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = (int(input('Qual é a sua opção? ')))

if opcao == 1:
    op1 = val - (val * 10 / 100)
    print('Sua compra de {:.2f} vai custar {:.2f} no final '.format(val, op1))
elif opcao == 2:
    novo = val - (val * 5 / 100)
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(val, novo))
elif opcao == 3:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(val, val))
elif opcao == 4:
    op4 = val + (val * 20 / 100)
    par = int(input('Quantas parcelas?'))
    juros = op4 / par
    print('Sua compra será parcelada de {}x de {:.2f} com juros'.format(par, juros))
    print('Sua compra de {:.2f} vai custar {:.2f} no final '.format(val, op4))
else:
    print('Opção invalida')