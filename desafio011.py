largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
soma = altura * largura
menos = soma / 2
print(f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {soma}m2')
print(f'Para pintar essa parede, você precisará de {menos}l de tinta.')
