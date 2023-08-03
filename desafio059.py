valor_um = int(input('Digite um valor: '))
valor_dois = int(input('Digite outro valor: '))
opc = 0
while opc != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair do Programa
    ''')
    opc = int(input('Qual é a sua opção? '))
    if opc == 1:
        resultado = valor_um + valor_dois
        print(f'A soma entre valor1 e valor2 é {resultado}')
    elif opc == 2:
        resultado_dois = valor_um * valor_dois
        print(f'O Multiplicador do valor 1 e valor 2 é {resultado_dois}')
    elif opc == 3:
        if valor_um > valor_dois:
            maior = valor_um
        else:
            maior = valor_dois  
        print(f'Entre {valor_um} e {valor_dois} o maior valor é {maior}')
    elif opc == 4:
        print('Informe os números novamente: ')
        valor_um = int(input('Digite outro valor: '))
        valor_dois = int(input('Digite Novamente Outro Valor: '))
    elif opc == 5:
        print('Finalizando.....')
    else:
        print('Opção Inválida!')
print('Fim do Programa! Volte sempre!')
