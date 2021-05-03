print('Gerador de PA')
print('-=-' * 10)

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

d = p 
c = 1
while c <= 10:
    print('{} -> '.format(d), end='')
    d += r
    c += 1
print('FIM')