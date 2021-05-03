kg = int((input('Qual é o seu pesp? (Kg) ')))
m = float(input('Qual é sua altura? (m) '))


imc = kg / m**2

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO! Você precisa comer mais')
elif imc > 18.5 and imc < 25:
    print('PESO IDEAL!')
elif imc > 25  and imc < 30:
    print('SOBREPESO')
elif imc > 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA! TOME CUIDADO ')
