soma_idade = soma_homem = soma_mulher = soma_idadeMulher = 0
while True:
    idade = int(input('Qual sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        soma_idade += 1
    if sexo == 'M':
        soma_homem += 1
    if sexo == 'F':
        soma_mulher += 1
    if sexo == 'F' and idade < 20:
        soma_idadeMulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
        print('=-=' * 15)
    if resp == 'N':
        break
print(f'Tem {soma_idade} Pessoas Maiores de 18 anos.')
print(f'Tem {soma_homem} Homens cadastrados no Programa.')
print(f'Tem {soma_mulher} Mulheres cadastradas no Programa.')
print(f'Tem {soma_idadeMulher} Mulheres menores de 20 Anos')
