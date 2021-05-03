cont = 0
v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o último número: '))

valores = (v1, v2, v3, v4)

print(f'Você digitou os valores {valores}')

print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'Os valores 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não aparece em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')