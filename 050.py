soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite números pares: '))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma  + n
    else:
        print('Os valores de impar no são somados')
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))        