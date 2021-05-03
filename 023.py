''' Faça um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos digitos separados. 
Digite um numero:1834
unidade:4 dezena:3 centena:8 milhar:1'''

num = int(input('Informe um número: '))

n = str(num) # Ele esta armazenado o numero igual a um nome 

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))