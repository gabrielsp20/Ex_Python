''' O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos.Faça um programa que leia 
o nome dos quatros alunos e mostre a ordem sorteada. '''



from random import shuffle

aluno1 = (input('Primeiro aluno:'))
aluno2 = (input('Segundo aluno:'))
aluno3 = (input('Terceiro aluno:'))
aluno4 = (input('Quarto aluno:'))

tira = str(input('Quem vai sair da lista? '))

lista = [aluno1, aluno2, aluno3, aluno4]

if tira == lista:
    del(lista[lista])
    


shuffle(lista)

print('A ordem apresentada será ')
print(lista)