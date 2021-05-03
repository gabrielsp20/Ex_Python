'''Faça um algoritmo que leia salário de um funcionário
e mostre seu novo salário, com 15% de aumento.'''






sal = float(input('Qual é o salário do funcionario? R$'))

novosal = sal + (sal * 15 / 100)

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(sal,novosal))