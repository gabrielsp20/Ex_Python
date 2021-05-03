a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
# Verificar quem é o menor
menor = a
if b<a and b<c:
    menor = b
elif c<a and c<b:
    menor = c
# Verificar quem é o menor

maior = a
if b>a and b>c: 
    maior = b
elif c>a and c>b:
    maior = c
print('O menor valor dgitado foi {}'.format(menor))
print('O maior valor dgitado foi {}'.format(maior))