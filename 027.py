n = str(input('Digite sue nome completo:')).strip()

nome = n.split() #A funçao split separa o nome em blocos  ex:[Aline] [Silva] [Santos] [Ferreira]
print('Muito przer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) #Quantas posições de nome 0 até ... -1 pq ele conta o 0