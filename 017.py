''' Faça um programa que leia o comprimento do cateto oposto
 e do cateto adjacente de um triangulo ratângulo, calcule e mostre
 o comprimento da hipotenusa. '''



from math import hypot

co = float(input('Comprimento do cateto aposto:'))
ca = float(input('Comprimento do cateto adjacente:'))

h1 = hypot(co, ca)

print('A hipotenusa vai medir{:.2f}'.format(h1))