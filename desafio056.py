somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for pess in range(1, 5):
    print(f"---- {pess}ª PESSOA ----")
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()
    somaidade += age
    if pess == 1 and sex in 'Mm':
        maioridadehomem = age
        nomevelho = name
    if sex in 'Mm' and age > maioridadehomem:
        maioridadehomem = age
        nomevelho = name
    if sex in 'Ff' and age > 20:
        totmulher += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')
