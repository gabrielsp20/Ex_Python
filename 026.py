''' Faça um programa que leia uma frase pelo teclado e mostre:
> Quantos vezes apareceu a letra "A" 
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.'''


frase = str(input('Digite uma frase: ')).upper()

print('A letra A aparece {} vezes nessa frase.'.format(frase.count('A')))#Vai mostrar quantas letras tem na frase
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))#Em qual posição se encontra a primeira letra A
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))#Em qual posiçao se encotra a ultima letra A