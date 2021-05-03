vogais = ('aprender','programar', 'linguagem','python','curso','gratis')

for p in vogais:
    print(f'\nNa palavra {p.upper()} temos', end='' )
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')