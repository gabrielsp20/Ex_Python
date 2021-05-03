''' Crie um programa que leia o nome completo de uma pessoa e
mostre:
> O nome com todas as letras maisculas e minusculas.
> Quantas letras ao todo (sem considerar espaços)
> Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo:')).strip() # A função strip tira qualquer espaço indesejado 

print('Analisando seu nome.......')
print('Seu nome em maiúsculo é {}'.format(nome.upper())) # upper faz a palavra ficar maiúscula

print('Seu nome em minúsculo é {}'.format(nome.lower())) # lower faz a palavra ficar minúscula

print('Seu nome tem ao todo {} letras'.format(nome.count('')))# count conta todos os caracteres de uma frase

separa = nome.split()# Armazena sua frase me blocos 

print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
# nessa função ele mostrar seu primeiro nome e quantas letras
                                                                                    
