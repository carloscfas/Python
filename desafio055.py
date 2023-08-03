#peso = float(input('Qual é o seu peso? (Kg): '))
#altura = float(input('Qual é sua altura? (m): '))
#imc = peso / (altura ** 2)
#print(f'O IMC dessa pessoa é de {imc}')
#if imc < 18.5:
#   print('Abaixo do Peso')
#elif 18.5 <= imc < 25:
#    print('Peso Ideal')
#elif 25 <= imc < 30:
#    print('SobrePeso')
#elif 30 <= imc < 40:
#    print('Obesidade')
#else:
#    print('Obesidade Mórbida')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
