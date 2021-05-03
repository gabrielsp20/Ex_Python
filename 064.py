soma = 0
n = 0
tot = -1
while n != 999:
    if n != 999:
        soma += n 
        tot += 1  
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(tot, soma))