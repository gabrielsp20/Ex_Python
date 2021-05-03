''' Escreva um program que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem: 
-O primero valor é maior 
-O Segundo valor é maior
-Não existe valor maior, os dois são iguais'''



num = int(input('Primeiro número: '))
num2 = int(input('Primeiro número: '))

if num > num2:
    print('O PRIMEIRO número é maior')
elif num < num2:
    print('O SEGUNDO numero é maior')
elif num == num2:
    print('Os números são iguais ')
else:
    print('Não existe valor')