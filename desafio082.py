lista = []
lista_dois = []
lista_tres = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0: #par
        lista_dois.append(v)
    elif v % 2 == 1: #ímpar
        lista_tres.append(v)
print('-=' * 20)

print(f'Primeira lista foi {lista}')
print(f'Lista de pares foi {lista_dois}')
print(f'Lista de  ímpares foi {lista_tres}')
