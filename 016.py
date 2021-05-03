''' Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção inteira  '''



from math import trunc
num = (float(input('Digite um valor:')))

quebrar = trunc(num)

print('O valor digitado foi {} e a sua porção inteira é 9'.format(num, quebrar))