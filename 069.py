print('-' * 30)
print('CADASTRAR UMA PESSOA')
print('-' * 30)
cont = contm = contf = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('SEXO: [M/F]')).upper().strip()
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    print('-' * 30)
    print('CADASTRAR UMA PESSOA')
    print('-' * 30)
    if idade >= 18:
        cont += 1
    if sexo =='M':
        contm += 1
    if sexo =='F' and idade < 20:
        contf += 1
    if continuar == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {cont} ')
print(f'Ao todo temos {contm} homens cadastrados')
print(f'E temos {contf} mulheres com menos de 20 anos ')



    

    