aluno = dict()
aluno['nome'] = str(input('Digite seu nome: '))
aluno['média'] = float(input(f'Qual é a média do {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 15)
for k, v in aluno.items():
    print(f'--- {k} é igual a {v}')
