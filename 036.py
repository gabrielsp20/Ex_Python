''' Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do Salário ou então o emprestimo será negado '''

casa = float(input('Qual é o valor da casa?'))
sal = float(input('Qual é o salário do comprador?'))
anos = int(input('Em quantos anos ele vai pagar a casa?'))

prestação = casa / (anos * 12)
valor = sal * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

if prestação <= valor:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')