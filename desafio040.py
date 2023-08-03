nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2} , a média do aluno é {media}')
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 or media == 7.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
