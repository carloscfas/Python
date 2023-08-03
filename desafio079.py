lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado! Não vou adicionar....')
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=-' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')
