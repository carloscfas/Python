salario = float(input('Qual é o valor do seu sálario? '))
print('Estamos calculando o valor do seu aumento!')
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava {salario} passa a ganhar {aumento}')
