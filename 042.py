from time import sleep
print('-=-' * 20)
print('<Analisando Triângulo>')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print('-=-' * 20)
print('Analisando os segmentos....')
sleep(3)
print('')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triângulo!', end=' ')
    if r1 == r2 == r3:
        print('EQUILAERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')