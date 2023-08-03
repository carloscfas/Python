casa = float(input('valor da casa: R$ '))
salario = float(input('Salário do comprador: R$'))
financiamento = float(input('Quantos anos de financiamento? '))
prestacao = casa / (financiamento * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma cansa de {casa} em {financiamento} anos a prestação será de {prestacao}')
if prestacao <= minimo:
    print('Seu Empréstimo foi Aprovada!')
else:
    print('Seu Empréstimo foi Recusada!')
