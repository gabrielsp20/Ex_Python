print('=' * 10)
print('10 TEMOS DE UMA PA')
print('=' * 10)

p = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
d = p + (10 - 1) * r
for c in range(p,d + r,r):
    print( '{} ' .format(c), end='-> ')
print('ACABOU!!!')