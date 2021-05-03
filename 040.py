nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota + nota2) / 2

print('Tirando {} e {} a media do aluno é {:.1f}'.format(nota, nota2, media))

if media == 10.0:
    print('APROVADO! Você e um otimo aluno')
elif media >= 7.0:
    print('APROVADO! Nós vemos no proxima série')
elif media >= 5.0 or media == 6.9:
    print('RECUPERAÇÃO! Calma que você ainda tem chance')
elif media <= 5.0:
    print('REPROVADO! Infelizmente você vai repitir a série')