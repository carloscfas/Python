peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('SobrePeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
