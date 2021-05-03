t = 0
while True:
    print('=' * 20)
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
         break
    print('=' * 20)
    for c in range(1 , 11):
        print(f'{t} x {c} = {t*c} ')

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')  