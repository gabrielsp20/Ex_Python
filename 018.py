''' Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse angulo. '''


from math import sin,tan,cos,radians

angulo = float(input('Digite o ângulo que você deseja:'))

seno = sin(radians(angulo))
cosse = cos(radians(angulo))
tange = tan(radians(angulo))


print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosse))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo,tange))