sexo = str(input('Digite seu Sexo: [M/F]')).upper()[0] .strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por Favor, Informe seu sexo: ')) .strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
