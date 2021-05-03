from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))


opcao = 0
while opcao != 5:
    sleep(1)
    print('=' * 25)
    
    print('''[1] somar 
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    print('=' * 25)
    sleep(2)
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {} '.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('Os números são iguais')
    elif opcao == 4:
            print('Informe o número novamente:')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo Valor: '))
    elif opcao > 5:
        print('Opção inválida. Tente novamente')
print('Finalizando....')
sleep(2)    
print('Fim do programa! Volte sempre!')
    
