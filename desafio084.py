dados = []
grupo = []
cont = 0
maior = menor = 0
while True:
    dados.append(str(input('Digite um nome: ')))
    cont += 1
    dados.append(float(input('Digite seu peso:')))
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.append(int(input('Digite sua idade: ')))
    grupo.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]')).upper().title()
    if continuar in 'Nn':
        break

print('-=' * 20)
print(f'Foram cadastradas {cont} Pessoas no Programa do Carlos')
print(f'O maior peso foi de {maior}Kg, Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg, Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
