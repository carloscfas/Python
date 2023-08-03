lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    r = str(input('Quer Continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 20)
lista.sort(reverse=True)
if 5 in lista:
    print(f'O valor 5 foi Digitado')
else:
    print('O valor 5 não foi digitado!!')
print(f'Foram contados {cont} números da lista')
print(f'A lista em ordem Decrescente {lista}')
