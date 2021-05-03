print('Gerador de PA')
print('-=-' * 10)

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

d = p 
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(d), end='') 
        d += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))