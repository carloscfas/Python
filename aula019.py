""" pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas.items())
#print(pessoas.values())
#print(pessoas.keys())
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#del pessoas ['sexo']         = del usa para apagar
#pessoas['peso'] = '98.5'     = no lugar do append
for k, v in pessoas.items():
    print(f'{k} = {v}') """

""" brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla']) """

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
